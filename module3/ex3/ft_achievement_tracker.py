import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        'First Steps',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Unstoppable',
        'Sharp Mind',
        'Hidden Path Finder'
    ]
    count = random.randint(5, len(all_achievements))
    return set(random.sample(all_achievements, count))


def main():
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice.union(bob).union(charlie).union(dylan)
    print(f"\nAll distinct achievements: {all_distinct}\n")

    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"Common achievements: {common}\n")

    only_alice = alice.difference(bob.union(charlie).union(dylan))
    only_bob = bob.difference(alice.union(charlie).union(dylan))
    only_charlie = charlie.difference(alice.union(bob).union(dylan))
    only_dylan = dylan.difference(alice.union(bob).union(charlie))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    all_achievements = {
        'First Steps',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Unstoppable',
        'Sharp Mind',
        'Hidden Path Finder'
    }

    alice_missing = all_achievements.difference(alice)
    bob_missing = all_achievements.difference(bob)
    charlie_missing = all_achievements.difference(charlie)
    dylan_missing = all_achievements.difference(dylan)

    print(f"\nAlice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
