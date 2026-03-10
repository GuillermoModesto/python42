#!/usr/bin/env python3

class Flower():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        print(f"Created: {self.name} ({self.age}cm, {self.age} days)")

    def grow(self) -> None:
        self.height += 1
        self.growth += 1

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
        print(f"Growth this week: +{self.growth}cm")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    i = 0
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    for name, height, age in plant_data:
        plants.append(Flower(name, height, age))
        i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    main()
