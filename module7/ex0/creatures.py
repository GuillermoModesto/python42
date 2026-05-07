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
