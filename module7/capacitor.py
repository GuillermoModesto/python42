import ex1


def main():
    print("Testing Creature with healing capability")
    creatureFactory = ex1.HealingCreatureFactory()

    print(" base:")
    sproutling = creatureFactory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print(" evolved:")
    bloomelle = creatureFactory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")
    creatureFactory = ex1.TransformCreatureFactory()

    print(" base:")
    shiftling = creatureFactory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print(" evolved:")
    morphagon = creatureFactory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


if __name__ == "__main__":
    main()
