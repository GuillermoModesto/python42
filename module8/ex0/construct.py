import os
import site
import sys


def in_virtualenv() -> bool:
    return sys.base_prefix != sys.prefix


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def get_site_packages_path() -> str:
    try:
        site_packages: list[str] = site.getsitepackages()
    except (AttributeError, OSError):
        return "Unable to determine site-packages path"

    if site_packages:
        return site_packages[0]
    return "Unable to determine site-packages path"


def main() -> None:
    print()

    if in_virtualenv():
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()

        print("Package installation path:")
        print(get_site_packages_path())

    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows")
        print()
        print("Then run this program again.")

    print()


if __name__ == "__main__":
    main()
