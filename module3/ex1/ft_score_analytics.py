from sys import argv


def main():
    print("=== Player Score Analytics ===")
    if (len(argv) == 1):
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
            )
        return
    try:
        scores = [int(x) for x in argv[1:]]
        print(f"Scores processed: {scores}")
        argc = len(scores)
        print(f"Total players: {argc}")
        print(f"Total score: {sum(int(x) for x in scores)}")
        print(f"Average score: {sum(int(x) for x in scores) / argc}")
        print(f"Low score: {int(min(scores))}")
        print(f"High score: {int(max(scores))}")
        print(f"Score range: {int(max(scores)) - int(min(scores))}")
    except ValueError:
        print("Error: all values need to be a number.")


if __name__ == "__main__":
    main()
