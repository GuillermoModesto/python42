import importlib
import sys

REQUIRED_PACKAGES: list[str] = ["pandas", "numpy", "matplotlib"]

PACKAGE_DESCRIPTIONS: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> list[str]:
    missing: list[str] = []

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
        except ImportError:
            print(f"[MISSING] {package}")
            missing.append(package)
            continue

        version = getattr(module, "__version__", "unknown")
        desc = PACKAGE_DESCRIPTIONS.get(package, "Ready")
        print(f"[OK] {package} ({version}) - {desc}")

    return missing


def show_install_help() -> None:
    print()
    print("Missing dependencies detected.")
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("  poetry install")
    print()


def explain_pip_vs_poetry() -> None:
    print("Dependency Management:")
    print("- pip reads dependencies from requirements.txt")
    print("- Poetry reads dependencies from pyproject.toml")
    print("- Poetry also creates and manages the virtual environment")
    print("  for you, pip only installs into whatever is active")
    print()


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")

    data_size = 1000
    print(f"Processing {data_size} data points...")

    # numpy is the source of the data: a noisy sine wave.
    signal = np.sin(np.arange(data_size) * 0.05) * 50
    signal = signal + np.random.normal(0, 10, data_size)

    # pandas wraps the array so we can compute one summary stat.
    series = pd.Series(signal)
    print(f"Mean signal strength: {series.mean():.2f}")

    # matplotlib draws a single line chart of the data.
    plt.figure()
    plt.plot(series, color="green")
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    missing = check_dependencies()

    if missing:
        show_install_help()
        sys.exit(1)

    print()
    explain_pip_vs_poetry()
    analyze_matrix_data()


if __name__ == "__main__":
    main()
