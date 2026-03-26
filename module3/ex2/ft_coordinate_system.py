import math


def get_player_pos():
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            res = []
            for coord in parts:
                res.append(round(float(coord), 1))
            return tuple(res)
        except ValueError as e:
            print(
                f"Error on parameter, {e}"
                )


def main():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coords1 = get_player_pos()
    print(f"Got a first tuple: {coords1}")
    print(f"It includes: X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}")
    to_center = math.sqrt((coords1[0])**2 + (coords1[1])**2 + (coords1[2]**2))
    print(
        "Distance to center: "
        f"{round(to_center, 4)}\n"
        )

    print("Get a second set of coordinates")
    coords2 = get_player_pos()
    dist = math.sqrt(
        (coords2[0] - coords1[0])**2
        + (coords2[1] - coords1[1])**2
        + (coords2[2] - coords1[2])**2
        )
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    main()
