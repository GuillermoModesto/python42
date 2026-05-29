import sys
import os
import site


def in_virtualenv():
    return (
        (sys.base_prefix != sys.prefix)
    )


def get_venv_name():
    return os.path.basename(sys.prefix)


def main():
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

        site_packages = site.getsitepackages()

        if site_packages:
            print(site_packages[0])
        else:
            print("Unable to determine site-packages path")

    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows")
        print()
        print("Then run this program again.")

    print()


if __name__ == "__main__":
    main()
