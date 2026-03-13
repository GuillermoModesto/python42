from sys import argv, maxsize


def main():
    print("=== Inventory System Analysis ===")
    inventory = {}
    for i in argv[1:]:
        try:
            inventory.update({i.split(":")[0]: int(i.split(":")[1])})
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
    most_abundant = ""
    i = 0
    for key, value in inventory.items():
        if value > i:
            i = value
            most_abundant = key
    least_abundant = ""
    i = maxsize
    for key, value in inventory.items():
        if value < i:
            i = value
            least_abundant = key
    print("\n=== Inventory Statistics ===")
    if i != 0 and inventory:
        print("Most abundant: "
              f"{most_abundant} ({inventory[most_abundant]} units)"
              )
        print("Least abundant: "
              f"{least_abundant} ({inventory[least_abundant]} units)"
              )
    print("\n=== Item Categories ===")
    moderate_items = {
        key: value
        for key, value in inventory.items()
        if value >= 5
    }
    rare_items = {
        key: value
        for key, value in inventory.items()
        if value < 5
    }
    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {rare_items}")
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    restock = {key: value for key, value in inventory.items() if value <= 1}
    i = 0
    for key, value in restock.items():
        if i == len(restock) - 1:
            print(key)
        else:
            print(key, end=", ")
        i += 1
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    i = 0
    for key, value in inventory.items():
        if i == len(inventory) - 1:
            print(key)
        else:
            print(key, end=", ")
        i += 1
    print("Dictionary values: ", end="")
    i = 0
    for key, value in inventory.items():
        if i == len(inventory) - 1:
            print(value)
        else:
            print(value, end=", ")
        i += 1
    word = 'sword'
    print(f"Sample lookup - {word} in inventory: {word in inventory}")


if __name__ == "__main__":
    main()
