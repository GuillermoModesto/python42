from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5,
        max_length=15,
    )

    timestamp: datetime

    location: str = Field(
        min_length=3,
        max_length=100,
    )

    contact_type: ContactType

    signal_strength: float = Field(
        ge=0.0,
        le=10.0
    )

    duration_minutes: int = Field(
        ge=1,
        le=1440
    )

    witness_count: int = Field(
        ge=1,
        le=100
    )

    message_received: Optional[str] = Field(
        default=None,
        max_length=500
    )

    is_verified: bool = False

    @model_validator(mode='after')
    def validate_id(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID must start with AC")
        return self

    @model_validator(mode='after')
    def validate_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def validate_telepath(self) -> "AlienContact":
        # Telepathic contact needs at least 3 witnesses to be taken
        # seriously: fail when there are FEWER than 3, not more.
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode='after')
    def validate_message_signal(self) -> "AlienContact":
        if (self.signal_strength > 7
                and not self.message_received):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def print_alien(alien: AlienContact) -> None:
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type.value}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    if alien.message_received:
        print(f"Message: '{alien.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        valid_contact = AlienContact(
            contact_id='AC_2024_001',
            timestamp='2024-01-20T00:00:00',  # type: ignore[arg-type]
            location='Area 51, Nevada',
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli',
            is_verified=False
        )

        print("Valid contact report:")
        print_alien(valid_contact)

    except ValidationError as error:
        print(error)

    try:
        # Telepathic contact with only 2 witnesses: must fail the
        # "at least 3 witnesses" rule.
        invalid_contact = AlienContact(
            contact_id='AC_2024_002',
            timestamp='2024-02-14T00:00:00',  # type: ignore[arg-type]
            location='Roswell, New Mexico',
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=2,
            is_verified=False
        )

        print("Valid contact report:")
        print_alien(invalid_contact)

    except ValidationError:
        print("\n======================================")
        print("Expected validation error:")
        print("Telepathic contact requires at least 3 witnesses")


if __name__ == "__main__":
    main()
