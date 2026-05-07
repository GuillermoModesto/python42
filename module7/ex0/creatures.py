from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return (
            f"{self.name} is a {self.type} type Creature"
        )


class Flameling(Creature):
    def __init__(self):
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self):
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self):
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self):
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self):
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self):
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self):
        self.name = "Torragon"
        self.type = "Water"

    def attack(self):
        return ("Torragon uses Hydro Pump!")


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):

    def create_base(self):
        return (
            Flameling()
        )

    def create_evolved(self):
        return (
            Pyrodon()
        )


class AquaFactory(CreatureFactory):

    def create_base(self):
        return (
            Aquabub()
        )

    def create_evolved(self):
        return (
            Torragon()
        )
