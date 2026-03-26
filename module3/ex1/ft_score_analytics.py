import sys


def main():
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
            )
        return
    scores = []
    for i in sys.argv[1:]:
        try:
            scores.append(int(i))
        except ValueError:
            print(f"Invalid parameter: {i}")
    if (len(scores) == 0):
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
            )
        return
    print(f"Scores processed: {scores}")
    argc = len(scores)
    print(f"Total players: {argc}")
    print(f"Total score: {sum(int(x) for x in scores)}")
    print(f"Average score: {sum(int(x) for x in scores) / argc}")
    print(f"Low score: {int(min(scores))}")
    print(f"High score: {int(max(scores))}")
    print(f"Score range: {int(max(scores)) - int(min(scores))}")


if __name__ == "__main__":
    main()
