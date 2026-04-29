from alchemy import create_air


def main():
    print("=== Alembic 5 ===")
    print(
        "Accessing alchemy/elements.py using 'from ... import ...' structure"
        )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
