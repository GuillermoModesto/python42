from sys import argv, maxsize


def main():
    print("=== Inventory System Analysis ===")
    inventory = {}
    for i in argv[1:]:
        try:
            if (i.split(":")[0] not in inventory):
                inventory.update({i.split(":")[0]: int(i.split(":")[1])})
            else:
                print(f"Redundant item {i.split(':')[0]} - discarding")
        except IndexError:
            print(f"Error - invalid parameter {i}")
        except ValueError as e:
            print(f"Quantity error for {i.split(':')[0]}: {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = 0
    for item in inventory.values():
        total += item
    print(f"Total quantity of the {len(inventory.keys())} items: {total}")
    for key, value in inventory.items():
        print(f"Item {key} represents ({value / total * 100}%)")
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
    if i != 0 and inventory:
        print("Item most abundant: "
              f"{most_abundant} with quantity {inventory[most_abundant]}"
              )
        print("Item least abundant: "
              f"{least_abundant} with quantity {inventory[least_abundant]}"
              )
    inventory.update({"hate": 99999})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
