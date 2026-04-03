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
        text = f.read()
        print(
            "---\n"
            f"\n{text}\n"
            "---"
        )
        f.close()
        print(f"File {sys.argv[1]} closed.\n")

        print("Transform data:\n---\n")
        new_text = ""
        for line in text.splitlines():
            new_text += line + "#" + "\n"
        print(new_text)
        print("---")
        new_file = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
            return
        print(f"Saving data to '{new_file}'")
        try:
            file = open(new_file, "w")
            file.write(new_text)
            file.close()
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"Error opening file '{new_file}': {e}")
            print("Data not saved.")
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
