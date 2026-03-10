def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        open("Larali Larila")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    print("Testing KeyError...")
    try:
        {"a": 1}["b"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
        open("Larali Larila")
        {"a": 1}["b"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested succesfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
