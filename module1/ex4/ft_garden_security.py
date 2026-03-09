#!/usr/bin/env python3

class Flower():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        print(f"Plant created: {self.name}")

    def set_height(self, new_height: int) -> None:
        if (new_height >= 0):
            self.height = new_height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(f"Invalid operation: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:
        if (new_age >= 0):
            self.age = new_age
            print(f"Age updated: {self.age}cm [OK]")
        else:
            print(f"\nInvalid operation: age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_info(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


def main():
    print("=== Garden Security System ===")
    plant = Flower("Rose", 10, 5)
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    print("")
    plant.get_info()


if __name__ == "__main__":
    main()
