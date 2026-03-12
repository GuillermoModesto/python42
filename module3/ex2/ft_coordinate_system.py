from math import sqrt


def main():
    print("=== Game Coordinate System ===\n")
    coords = tuple((10, 20, 5))
    print(f"Position created: {coords}")
    print(
        "Distance between (0, 0, 0) and "
        f"{coords}: "
        f"{sqrt((coords[0])**2 + (coords[1])**2 + (coords[2]**2))}\n"
        )
    coords = "3,4,0"
    print(f"Parsing coordinates: \"{coords}\"")
    coords = tuple([int(x) for x in coords.split(",")])
    print(f"Parsed position: {coords}")
    print(
        "Distance between (0, 0, 0) and "
        f"{coords}: "
        f"{sqrt((coords[0])**2 + (coords[1])**2 + (coords[2]**2))}\n"
        )
    coords2 = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{coords2}\"")
    try:
        coords2 = tuple([int(x) for x in coords2.split(",")])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
    print("\nUnpacking demonstration:")
    print(f"Player at: x={coords[0]}, y={coords[1]}, z={coords[2]}")
    print(f"Coordinates: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


if __name__ == "__main__":
    main()
