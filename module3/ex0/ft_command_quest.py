from sys import argv


def main():
    print("=== Command Quest ===")
    argc = len(argv)
    i = 1
    if (argc == 1):
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argc - 1}")
        while (i < argc):
            print(f"Argument {i}: {argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
