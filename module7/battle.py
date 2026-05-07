import ex0


def test_factory(factory):
    """Works with any factory - no knowledge of specific creatures needed."""
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1, factory2):
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(f"{base1.describe()} \n vs. \n{base2.describe()} \n fight!")
    print(base1.attack())
    print(base2.attack())


def main():
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("\nTesting factory")
    test_factory(aqua_factory)

    print("\nTesting battle")
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()