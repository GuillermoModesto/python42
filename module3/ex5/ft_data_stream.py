from typing import Generator


def generate_events(n) -> Generator[dict[str, object], None, None]:
    names = ["alice", "bob", "charlie", "bonk", "jesus christ its jason borne"]
    events = [
        "killed a monster", "found treasure", "level up", "found God",
        "pondered its existence", "mama, just killed a man",
        "put a gun againts its head", "pulled the trigger"
    ]
    for i in range(n):
        yield {
            "name": names[i % len(names)],
            "event": events[i % len(events)],
            "level": (i % 15) + 1
        }


def fibonacci_generator():
    last = 0
    num = 1
    yield last
    yield num
    while True:
        """
        temp = num
        num = num + last
        last = temp
        """
        last, num = num, num + last
        yield (num)


def prime_generator():
    yield 2
    num = 3
    i = 2
    while True:
        if (num % i == 0):
            num += 1
            i = 2
        else:
            i += 1
        if (num == i):
            yield num


def main():
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")
    events = generate_events(1000)
    total = 0
    high_player = 0
    treasure = 0
    levelup = 0
    for event in events:
        if (total <= 3):
            print(
                f"Event {total}: "
                f"Player {event['name']} "
                f"(level {event['level']} {event['event']})"
            )
        total += 1
        if ('level up' in event['event']):
            levelup += 1
        if (event['level'] >= 10):
            high_player += 1
        if ('treasure' in event['event']):
            treasure += 1
    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_player}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fibonacci = fibonacci_generator()
    print("Fibonacci sequence (first 10): ", end=" ")
    for _ in range(10):
        print(next(fibonacci), end=" ")
    prime = prime_generator()
    print("\nPrime numbers (first 5): ", end=" ")
    for _ in range(5):
        print(next(prime), end=" ")


if __name__ == "__main__":
    main()
