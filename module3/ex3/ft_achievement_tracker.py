def main():
    print("=== Achievement Tracker System ===\n")
    alice_achievements = set(
        ('first_kill', 'level_10', 'treasure_hunter', 'speed_demon')
        )
    bob_achievements = set(
        ('first_kill', 'level_10', 'boss_slayer', 'collector')
        )
    charlie_achievements = set(
        ('level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
            'perfectionist')
        )
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print("\n=== Achievement Analytics ===")
    unique = alice_achievements.union(bob_achievements)
    unique = unique.union(charlie_achievements)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    common = alice_achievements.intersection(bob_achievements)
    common = common.intersection(charlie_achievements)
    print(f"\nCommon to all players: {common}")
    alice_rare = alice_achievements.difference(
        bob_achievements.union(charlie_achievements)
        )
    bob_rare = bob_achievements.difference(
        alice_achievements.union(charlie_achievements)
        )
    charlie_rare = charlie_achievements.difference(
        alice_achievements.union(bob_achievements)
        )
    rare_achievements = alice_rare.union(bob_rare).union(charlie_rare)
    print(f"Rare achievements (1 player):{rare_achievements}")
    alice_bob = alice_achievements.intersection(bob_achievements)
    print(f"\nAlice vs Bob common: {alice_bob}")
    aux = alice_achievements.union(bob_achievements)
    alice_unique = aux.difference(bob_achievements)
    bob_unique = aux.difference(alice_achievements)
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
