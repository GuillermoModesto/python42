class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


def main():
    test_custom_errors()


if __name__ == "__main__":
    main()
