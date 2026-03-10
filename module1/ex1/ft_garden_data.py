#!/usr/bin/env python3

class Flower():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(plants: list[Flower]) -> None:
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def main():
    ft_garden_data(
        [
            Flower("Rose", 25, 30),
            Flower("Sunflower", 80, 45),
            Flower("Cacus", 15, 120)
        ]
    )


if __name__ == "__main__":
    main()
