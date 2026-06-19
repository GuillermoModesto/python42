import ex1
from ex0 import CreatureFactory


def test_healing_factory(factory: CreatureFactory) -> None:
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, ex1.HealCapability):
            print(creature.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, ex1.TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    heal_factory = ex1.HealingCreatureFactory()
    test_healing_factory(heal_factory)

    print()
    print("Testing Creature with transform capability")
    transform_factory = ex1.TransformCreatureFactory()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
