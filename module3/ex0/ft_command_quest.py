import sys


def main():
    print("=== Command Quest ===")
    argc = len(sys.argv)
    i = 1
    print(f"Program name: {sys.argv[0]}")
    if argc != 1:
        print(f"Arguments received: {argc - 1}")
    else:
        print("No arguments provided!")
    while (i < argc):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
