def generate_game_events(n):
    names = ["alice", "bob", "charlie", "monko", "gonko"]
    actions = ["killed monster", "found treasure", "leveled up",
               "pondered its existence", "found God"]
    for i in range(n):
        nm = names[i % len(names)]
        level = (i % 15) + 1
        act = actions[i % len(actions)]
        event = f"Player {nm} (level {level}) {act}"
        yield (event, level, act)


def main():
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")
    events = generate_game_events(1000)
    total = 0
    treasure = 0
    levelup = 0
    high_level = 0
    for event in events:
        event_text = event[0]
        level = event[1]
        action_data = event[2]
        total += 1
        if total <= 5:
            print(f"Event {total}: {event_text}")
        if level >= 10:
            high_level += 1
        if action_data == "found treasure":
            treasure += 1
        if action_data == "leveled up":
            levelup += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")


if __name__ == "__main__":
    main()
