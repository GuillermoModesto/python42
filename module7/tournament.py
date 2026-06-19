from typing import List, Tuple
import ex0
import ex1
import ex2


Opponent = Tuple[ex0.CreatureFactory, ex2.BattleStrategy]


def opponent_name(opponent: Opponent) -> str:
    factory, strategy = opponent
    creature = factory.create_base()
    return f"({creature.name}+{strategy})"


def battle(opponents: List[Opponent]) -> None:
    print("[ " + ", ".join(opponent_name(op) for op in opponents) + " ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]

                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()

                print("* Battle *")
                print(creature_a.describe())
                print("vs.")
                print(creature_b.describe())
                print("now fight!")

                strategy_a.act(creature_a)
                strategy_b.act(creature_b)

    except ex2.InvalidBattleStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    fire_fact = ex0.FlameFactory()
    aqua_fact = ex0.AquaFactory()
    heal_fact = ex1.HealingCreatureFactory()
    trans_fact = ex1.TransformCreatureFactory()

    normal_strat = ex2.NormalStrategy()
    aggressive_strat = ex2.AggressiveStrategy()
    defensive_strat = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (fire_fact, normal_strat),
        (heal_fact, defensive_strat),
    ])

    print("Tournament 1 (error)")
    battle([
        (fire_fact, aggressive_strat),
        (heal_fact, defensive_strat),
    ])

    print("Tournament 2 (multiple)")
    battle([
        (aqua_fact, normal_strat),
        (heal_fact, defensive_strat),
        (trans_fact, aggressive_strat),
    ])


if __name__ == "__main__":
    main()
