#!/usr/bin/env python3

class Flower():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1

    def grow_age(self):
        self.age += 1

    def week(self):
        print("=== Day 1 ===")
        self.get_info()
        for i in range(0, 6):
            self.grow()
            self.grow_age()
        print("=== Day 7 ===")
        self.get_info()
        print(f"Growth this week: +{self.growth}cm\n")

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth(plant):
    plant.week()


def main():
    plants = [
        Flower("Rose", 25, 30),
        Flower("Cactus", 5, 90),
        Flower("Oak", 200, 365)
    ]
    for plant in plants:
        ft_plant_growth(plant)


if __name__ == "__main__":
    main()
