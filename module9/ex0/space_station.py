from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3,
        max_length=10,
    )

    name: str = Field(
        min_length=1,
        max_length=50,
    )

    crew_size: int = Field(
        ge=1,
        le=20
    )

    power_level: float = Field(
        ge=0.0,
        le=100.0
    )

    oxygen_level: float = Field(
        ge=0.0,
        le=100.0
    )

    last_maintenance: datetime

    is_operational: bool = True

    notes: Optional[str] = Field(
        default=None,
        max_length=200
    )


def print_station(station):
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    print("Status: ", end="")
    if (station.is_operational):
        print("Operational")
    else:
        print("Non operational")


def main():
    print("Space Station Data Validation")
    print("========================================")
    try:
        test = SpaceStation(
            station_id='LGW125',
            name='Titan Mining Outpost',
            crew_size=6,
            power_level=76.4,
            oxygen_level=95.5,
            last_maintenance='2023-07-11T00:00:00',
            is_operational=True,
            notes=None
        )

        print("Valid station created:")
        print_station(test)

    except ValidationError as e:
        print(e)
    try:
        test = SpaceStation(
            station_id='LGW125',
            name='Titan Mining Outpost',
            crew_size=22,
            power_level=76.4,
            oxygen_level=95.5,
            last_maintenance='2023-07-11T00:00:00',
            is_operational=True,
            notes=None
        )

        print("Valid station created:")
        print_station(test)

    except ValidationError:
        print("\n========================================")
        print("Expected validation error:")
        print("Input should be less than or equal to 20")


if __name__ == "__main__":
    main()
