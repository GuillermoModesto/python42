def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
    try:
        if (plant_name == "" or plant_name is None):
            raise ValueError("Error: Plant name cannot be empty!")
        if (water_level > 10):
            raise ValueError(
                f"Error: Water level {water_level} is to high! (max 10)"
                )
        if (water_level < 1):
            raise ValueError(
                f"Error: Water level {water_level} is to low! (min 1)"
                )
        if (sunlight_hours > 12):
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is to high! (max 12)"
                )
        if (sunlight_hours < 2):
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is to low! (min 2)"
                )
        print(f"Plant {plant_name} is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 4, 4)
    print("\nTesting empty plant name...")
    check_plant_health(None, 3, 3)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 0, 3)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 1)
    print("\nAll error raising tests completed!")


def main():
    test_plant_checks()


if __name__ == "__main__":
    main()
