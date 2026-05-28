import sys
import importlib


REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "matplotlib",
]


def check_dependencies():
    loaded_packages = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")

            if package == "pandas":
                desc = "Data manipulation ready"
            elif package == "numpy":
                desc = "Numerical computation ready"
            elif package == "matplotlib":
                desc = "Visualization ready"
            else:
                desc = "Ready"

            print(f"[OK] {package} ({version}) - {desc}")

            loaded_packages[package] = module

        except ImportError:
            print(f"[MISSING] {package}")

    return loaded_packages


def show_install_help():
    print()
    print("Missing dependencies detected.")
    print()

    print("Install with pip:")
    print("pip install -r requirements.txt")
    print()

    print("Install with Poetry:")
    print("poetry install")
    print()


def analyze_matrix_data(np, pd, plt):
    print()
    print("Analyzing Matrix data...")

    data_size = 1000

    print(f"Processing {data_size} data points...")

    timestamps = np.arange(data_size)

    signal_strength = (
        np.sin(timestamps * 0.05) * 50
        + np.random.normal(0, 10, data_size)
    )

    df = pd.DataFrame({
        "timestamp": timestamps,
        "signal_strength": signal_strength,
    })

    mean_signal = df["signal_strength"].mean()
    std_signal = df["signal_strength"].std()

    print(f"Mean signal strength: {mean_signal:.2f}")
    print(f"Standard deviation: {std_signal:.2f}")

    print()
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["timestamp"],
        df["signal_strength"],
        color="green",
        linewidth=1
    )

    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")

    plt.grid(True)

    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    packages = check_dependencies()

    missing = [
        pkg for pkg in REQUIRED_PACKAGES
        if pkg not in packages
    ]

    if missing:
        show_install_help()
        sys.exit(1)

    pd = packages["pandas"]
    np = packages["numpy"]
    plt = importlib.import_module("matplotlib.pyplot")

    print()
    print("Dependency Management:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml")
    print("- Poetry creates and manages virtual environments automatically")

    analyze_matrix_data(np, pd, plt)


if __name__ == "__main__":
    main()
