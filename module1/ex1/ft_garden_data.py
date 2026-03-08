#!/usr/bin/env python3

class Flower():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(plants):
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def main():
    plant1 = Flower("Rose", 25, 30)
    plant2 = Flower("Sunflower", 80, 45)
    plant3 = Flower("Cacus", 15, 120)
    plants = [plant1, plant2, plant3]
    ft_garden_data(plants)


if __name__ == "__main__":
    main()
