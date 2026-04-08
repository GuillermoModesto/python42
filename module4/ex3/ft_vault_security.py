from typing import Tuple


def secure_archive(
        file_name: str, action: str = "r", content: str = ""
        ) -> Tuple[bool, str]:
    try:
        with open(file_name, action) as f:
            if action == "r":
                data = f.read()
                return True, data
            elif action == "w":
                f.write(content if content else "")
                return True, "Write successful"
            else:
                return False, "Unsupported action"
    except (FileNotFoundError, PermissionError) as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {e}"


def main():
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    test1 = secure_archive("no")
    print(test1)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    test2 = secure_archive("/etc/master.passwd")
    print(test2)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    test3 = secure_archive("ancient_fragment.txt")
    print(test3)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    test4 = secure_archive(
        "new_ancient_fragment.txt", "w", "Content successfully written to file"
        )
    print(test4)


if __name__ == "__main__":
    main()
