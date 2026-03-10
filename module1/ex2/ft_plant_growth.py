#!/usr/bin/env python3

class Flower():
    def __init__(
            self, name: str, height: int, age: int, growth_rate: int = 1
            ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate
        self.growth = 0

    def grow(self) -> None:
        self.height += self.growth_rate
        self.growth += self.growth_rate

    def grow_age(self) -> None:
        self.age += 1

    def week(self) -> None:
        print("=== Day 1 ===")
        self.get_info()
        for i in range(0, 6):
            self.grow()
            self.grow_age()
        print("=== Day 7 ===")
        self.get_info()
        print(f"Growth this week: +{self.growth}cm\n")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth(plant: Flower) -> None:
    plant.week()


def main():
    plants = [
        Flower("Rose", 25, 30, 2),
        Flower("Cactus", 5, 90),
        Flower("Oak", 200, 365, 3)
    ]
    for plant in plants:
        ft_plant_growth(plant)


if __name__ == "__main__":
    main()
