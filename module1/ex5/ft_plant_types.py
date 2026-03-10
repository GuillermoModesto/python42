class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print("Rose is blooming beautifully!")

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(
            self, name: str, height: int, age: int, trunk_diameter: str
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Oak provides {self.trunk_diameter} square meters of shade")

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter} diameter"
        )


class Vegetable(Plant):
    def __init__(
        self, name: str,
        height: int, age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nut_value(self) -> None:
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )


def main():
    print("=== Garden Plant Types ===\n")
    flower = Flower("rose", 25, 30, "red")
    flower.get_info()
    flower.bloom()
    print("")
    tree = Tree("oak", 500, 1825, 50)
    tree.get_info()
    tree.produce_shade()
    print("")
    vegetable = Vegetable("tomato", 80, 90, "sumer", "vitamin C")
    vegetable.get_info()
    vegetable.nut_value()


if __name__ == "__main__":
    main()
