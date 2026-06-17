import functools
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'power' in kwargs:
                power = kwargs['power']
            elif args:
                power = args[-1]
            else:
                power = None

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError("Spell unstable")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def orc_warcry() -> str:
        return "Waaaaaaagh spelled !"

    print(orc_warcry())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X7"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == '__main__':
    main()
