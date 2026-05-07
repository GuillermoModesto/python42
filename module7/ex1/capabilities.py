from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex0.creatures import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.is_transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return ("Sproutling uses Vine Whip!")

    def heal(self):
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Normal")

    def attack(self):
        return ("Bloomelle uses Petal Dance!")

    def heal(self):
        return (f"{self.name} heals itself and others for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return (
            Sproutling()
        )

    def create_evolved(self):
        return (
            Bloomelle()
        )


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def attack(self):
        if self.is_transformed:
            return ("Shiftling performs a boosted strike!")
        else:
            return ("Shiftling attacks normally.")

    def transform(self):
        self.is_transformed = 1
        return ("Shiftling shifts into a sharper form!")

    def revert(self):
        self.is_transformed = 0
        return ("Shiftling returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self):
        if self.is_transformed:
            return ("Morphagon unleashes a devastating morph strike!")
        else:
            return ("Morphagon attacks normally.")

    def transform(self):
        self.is_transformed = 1
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self):
        self.is_transformed = 0
        return ("Morphagon stabilizes its form.")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return (
            Shiftling()
        )

    def create_evolved(self):
        return (
            Morphagon()
        )
