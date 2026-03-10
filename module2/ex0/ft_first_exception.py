def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if (temp < 0):
            raise ValueError(f"Error: {temp} is to cold for plants (max 40º)")
        elif (temp > 40):
            raise ValueError(f"Error: {temp} is to hot for plants (max 40º)")
        print(f"Temperature {temp} is perfect for plants!")
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    testing_values = ["25", "abc", "100", "-50"]
    for value in testing_values:
        print(f"Testing value: {value}")
        check_temperature(value)
        print("")
    print("All tests completed - program didn't crash!")


def main():
    test_temperature_input()


if __name__ == "__main__":
    main()
