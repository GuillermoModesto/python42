import sys


def main():
    if (len(sys.argv) != 2):
        print("Usage: python ft_ancient_text.py <filename>")
        return

    print("=== Cyber Archives Recovery ===\n")
    f = None
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        f = open(sys.argv[1], "r")
        print(
            "---\n"
            f"\n{f.read()}\n"
            "---"
        )
        f.close()
        print(f"File {sys.argv[1]} closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
