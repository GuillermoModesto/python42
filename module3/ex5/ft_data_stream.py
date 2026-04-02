from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use",
               "release"]

    while True:
        yield (
            players[random.randrange(len(players))],
            actions[random.randrange(len(actions))]
        )


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    for _ in range(len(events)):
        index = random.randrange(len(events))
        yield events.pop(index)


def main():
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = []
    for _ in range(10):
        event_list.append(next(stream))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
