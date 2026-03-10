class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        print(
            f"- {self.name.capitalize()}: {self.height}cm"
        )


class FloweringPlant(Plant):
    def __init__(
            self, name: str, height: int, age: int, color: str
            ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        print(
            "- "
            f"{self.name.capitalize()}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int,
        age: int, color: str, prize: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize = prize

    def get_info(self) -> None:
        print(
            "- "
            f"{self.name.capitalize()}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize}"
        )


class GardenManager():
    total_gardens = 0

    def __init__(
            self, manager: str, plants: list[Plant] = None, score: int = 0
            ) -> None:
        self.manager = manager
        self.score = score
        self.plants = [] if plants is None else plants
        self.plants_amount = 0
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plants(self, plants: list[Plant]) -> None:
        for plant in plants:
            self.plants.append(plant)
            if isinstance(plant, PrizeFlower):
                self.score += plant.prize
            self.plants_amount += 1
            print(f"Added {plant.name} to {self.manager}'s garden")

    def work(self) -> None:
        print(f"\n{self.manager} is helping all plants grow...")
        for plant in self.plants:
            self.total_growth += 1
            plant.grow()

    def add_score(self, add: int) -> None:
        self.score += add

    @classmethod
    def create_garden_network(
            cls, manager_info: list[dict]
            ) -> list["GardenManager"]:
        return [
            cls(
                manager["name"],
                manager["flowers"],
                manager["prize"]
                )
            for manager in manager_info
        ]

    class GardenStats():
        @staticmethod
        def get_manager_report(manager: "GardenManager") -> None:
            print(f"=== {manager.manager}'s Garden Report ===")
            print("Plants in garden:")
            for plant in manager.plants:
                plant.get_info()

        @staticmethod
        def get_plants_added(manager: "GardenManager") -> None:
            print(
                f"Plants added: {manager.plants_amount}, "
                f"Total growth: {manager.total_growth}cm"
            )

        @staticmethod
        def get_plant_types(manager: "GardenManager") -> None:
            regular = 0
            flowering = 0
            prize = 0
            for plant in manager.plants:
                if plant.__class__.__name__ == "Plant":
                    regular += 1
                elif plant.__class__.__name__ == "FloweringPlant":
                    flowering += 1
                elif plant.__class__.__name__ == "PrizeFlower":
                    prize += 1
                """
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1
                """
            print(
                "Plant types: "
                f"{regular} regular, "
                f"{flowering} flowering, "
                f"{prize} prize flowers"
            )

        @staticmethod
        def display_scores(managers: list["GardenManager"]) -> None:
            print("Garden scores - ", end="")
            for i, manager in enumerate(managers):
                if (i != len(managers) - 1):
                    print(f"{manager.manager}: {manager.score}, ", end="")
                else:
                    print(f"{manager.manager}: {manager.score}")

        @staticmethod
        def height_validation(height: int) -> None:
            print(f"Height validation test: {height >= 0}")


def main():
    print("=== Garden Management System Demo ===\n")
    managers = GardenManager.create_garden_network(
            [
                {
                    "name": "Alice",
                    "flowers": None,
                    "prize": 208
                },
                {
                    "name": "Bob",
                    "flowers": None,
                    "prize": 92
                }
            ]
        )
    managers[0].add_plants(
        [
            Plant("Oak Tree", 100, 300),
            FloweringPlant("Rose", 25, 7, "red"),
            PrizeFlower("Sunflower", 50, 15, "yellow", 10)
        ]
    )
    managers[0].work()
    print()
    managers[0].GardenStats.get_manager_report(managers[0])
    print()
    managers[0].GardenStats.get_plants_added(managers[0])
    managers[0].GardenStats.get_plant_types(managers[0])
    print()
    managers[0].GardenStats.height_validation(34)
    managers[0].GardenStats.display_scores(managers)


if __name__ == "__main__":
    main()
