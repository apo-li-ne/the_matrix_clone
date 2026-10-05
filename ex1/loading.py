import sys
from importlib import import_module
from importlib.metdata import version


def check_dependencies() -> list[str]:
   packages = ["pandas", "numpy", "matplotlib"]
   missing = []

   print("Checking dependencies:")

   for package in packages:
       try:
           import_module(package)
           print(f"[ok] {package} ({version(package)})")
        except ImportError:
           print(f"[MISSING] {package}")
           missing.append(package)

    return missing


def show_install_help(missing: list[str]) -> None:
    print("\nMissing packages:", ", ".join(missing))
    print()