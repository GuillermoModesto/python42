from sys import argv


def main():
    print("=== Inventory System Analysis ===")
    inventory = {}
    for i in argv[1:]:
        try:
            inventory.update({i[0]: int(i[2])})
        except ValueError as e:
            print(e)
    total = 0
    for item in inventory.values():
        total += item
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")
    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        print(f"{key}: {value} units ({value / total * 100}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {} ({} units")


if __name__ == "__main__":
    main()
