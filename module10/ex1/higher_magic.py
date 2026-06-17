from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def is_powerful_enough(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_result, heal_result = combined("Dragon", 50)
    print(f"Combined spell result: {fire_result}, {heal_result}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original:  {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_heal = conditional_caster(is_powerful_enough, heal)
    print(f"With power 25: {safe_heal('Dragon', 25)}")
    print(f"With power 5:  {safe_heal('Dragon', 5)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    for result in combo("Dragon", 20):
        print(result)

    print(f"\ncallable(fireball) -> {callable(fireball)}")
    print(f"callable('not a spell') -> {callable('not a spell')}")


if __name__ == '__main__':
    main()
