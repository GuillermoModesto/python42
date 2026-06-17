import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ['fire', 'ice', 'lightning']
    return {
        element: functools.partial(
            base_enchantment, power=50, element=element
        )
        for element in elements
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def cast_int(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def cast_str(spell: str) -> str:
        return spell

    @cast.register
    def cast_list(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment (power {power}) on {target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Empty list: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spells, 'divide')
    except ValueError as exc:
        print(f"Error handled: {exc}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    for element, enchant in enchanters.items():
        print(f"{element}: {enchant(target='Sword')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(f"Damage spell: {cast(42)}")
    print(f"Enchantment: {cast('fireball')}")
    print(f"Multi-cast: {cast([1, 2, 3])}")
    print(f"Unknown: {cast(3.14)}")


if __name__ == '__main__':
    main()
