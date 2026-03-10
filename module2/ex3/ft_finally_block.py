class Plant():
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        self.name = name
        self.height = height
        self.age = age


def water_plants(plant_list: list[Plant]) -> None:
    try:
        print("Open watering system")
        for plant in plant_list:
            print(f"Watering {plant.name}")
        print("Watering completed succesfully!")
    except Exception:
        print("Error: cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(
        [Plant("tomato"), Plant("lettuce"), Plant("carrot")]
    )
    print("\nTesting with error...")
    water_plants(
        [Plant("tomato"), None, Plant("carrot")]
    )
    print("\nCleanup always happens, even with errors!")


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
