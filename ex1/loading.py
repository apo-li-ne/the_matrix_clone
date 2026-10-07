import sys
from importlib import import_module
from importlib.metadata import version


PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def check_dependencies() -> list[str]:
    """Try to import each package and return the list of missing ones."""
    missing: list[str] = []
    print("Checking dependencies:")
    for name, role in PACKAGES.items():
        try:
            import_module(name)
            print(f"[OK] {name} ({version(name)}) - {role} ready")
        except ImportError:
            print(f"[MISSING] {name} - {role}")
            missing.append(name)
    return missing


def show_install_help(missing: list[str]) -> None:
    """Show which packages are missing and how to install them."""
    print("\nMissing packages:")
    for package in missing:
        print(f"  - {package}")
    print("\nInstall with pip:")
    print("  pip install -r requirements.txt")
    print("\nInstall with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def compare_tools() -> None:
    """Show the differences between pip and poetry."""
    print("\npip   -> requirements.txt, no lock file")
    print("Poetry -> pyproject.toml + poetry.lock, exact versions")


def analyse_and_plot() -> None:
    """Generate data with numpy, analyse with pandas, plot with matplotlib."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")
    data = pd.DataFrame({"signal": np.random.normal(50, 10, 1000)})
    print(f"Processing {len(data)} data points...")
    print(f"Mean signal: {data['signal'].mean():.2f}")

    print("Generating visualization...")
    data["signal"].plot(title="Matrix data")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Check dependencies, then run the analysis if evrything is there."""
    print("LOADING STATUS: Loading programs...\n")
    missing = check_dependencies()
    if missing:
        show_install_help(missing)
        sys.exit(1)
    analyse_and_plot()
    compare_tools()


if __name__ == "__main__":
    main()
