import sys


def main():
    print("=== Player Score Analytics ===")
    scores = sys.argv[1:]
    print(f"Scores processed: {scores}")
    argc = len(scores)
    print(f"Total players: {argc}")
    try:
        print(f"Total score: {sum(int(x) for x in scores)}")
    except ValueError as e:
        print(f"Total sum error: {e}")
    try:
        print(f"Average score: {sum(int(x) for x in scores) / argc}")
    except ValueError as e:
        print(f"Average score error: {e}")
    try:
        print(f"High score: {int(max(scores))}")
    except ValueError as e:
        print(f"High score error: {e}")
    try:
        print(f"Low score: {int(min(scores))}")
    except ValueError as e:
        print(f"Low score error: {e}")
    try:
        print(f"Score range: {int(max(scores)) - int(min(scores))}")
    except ValueError as e:
        print(f"Score range error: {e}")

if __name__ == "__main__":
    main()
