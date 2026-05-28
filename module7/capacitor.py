import ex1
from ex0.creatures import CreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creatures import Creature


def test_healing_factory(factory: CreatureFactory) -> None:
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
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
