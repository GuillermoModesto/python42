class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class Plant():
    def __init__(self, name: str, water: int = 0, sun: int = 0) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self, plants: list[Plant] = None) -> None:
        self.plants = [] if plants is None else plants

    def add_plants(self, new_plants: list[Plant]) -> None:
        try:
            print("Adding plants to garden...")
            for plant in new_plants:
                if (plant.name is None):
                    raise PlantError(
                        "Error adding plant: Plant name cannot be empty!"
                        )
                self.plants.append(plant)
                print(f"Added {plant.name} succesfully")
        except GardenError as e:
            print(e)

    def water_plants(self) -> None:
        try:
            print("\nOpen watering system")
            for plant in self.plants:
                plant.water += 1
                print(f"Watering {plant.name} - success")
            print("Watering completed succesfully!")
        except Exception:
            print("Error: cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if (plant.name == "" or plant.name is None):
                    raise ValueError("Error: Plant name cannot be empty!")
                if (plant.water > 10):
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water} is to high! (max 10)"
                        )
                if (plant.water < 1):
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water} is to low! (min 1)"
                        )
                if (plant.sun > 12):
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Sunlight hours {plant.sun} is to high! (max 12)"
                        )
                if (plant.sun < 2):
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        f"Sunlight hours {plant.sun} is to low! (min 2)"
                        )
                print(f"{plant.name}: "
                      f"healthy (water: {plant.water}, sun: {plant.sun})")
            except ValueError as e:
                print(e)


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    manager.add_plants(
        [
            Plant("tomato", 3, 3),
            Plant("lettuce", 14, 3),
            Plant(None, 3, 3),
        ]
    )
    manager.water_plants()
    manager.check_plant_health()
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


def main():
    test_garden_management()


if __name__ == "__main__":
    main()
