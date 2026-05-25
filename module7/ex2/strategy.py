from abc import ABC, abstractmethod
from typing import Any
from ex1.capabilities import TransformCapability, HealCapability


class InvalidBattleStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return True

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        creature.attack()

    def __str__(self) -> str:
        return "Normal"


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        if (isinstance(creature, TransformCapability)):
            return True
        return False
    
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        creature.transform()
        creature.attack()
        creature.revert()

    def __str__(self) -> str:
        return "Aggressive"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        if (isinstance(creature, HealCapability)):
            return True
        return False

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        creature.attack()
        creature.heal()

    def __str__(self) -> str:
        return "Defensive"