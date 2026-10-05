import os
import site
import sys


def is_in_venv() -> bool:
    """Return True if Python runs inside a virtual environment"""
    return sys.prefix != sys.base_prefix


def get_packages_path() -> str:
    """Return the path where packages are installed"""
    paths = site.getsitepackages()
    if paths:
        return paths[0]
    return "Unknown"


def show_outside_venv() -> None:
    """Display info when running in the global environment"""
    lines = [
        "MATRIX STATUS: You’re still plugged in\n",
        f"Current Python: {sys.executable}",
        "Virtual Environment: None detected\n",
        "WARNING: You’re in the global environment!",
        "The machines can see everything you install.\n",
        "To enter the construct, run:",
        "python -m venv matrix_env",
        "source matrix_env/bin/activate # On Unix",
        "matrix_env\\Scripts\\activate # On Windows\n",
        "Then run this program again."
    ]
    for line in lines:
        print(line)


def show_inside_venv() -> None:
    """Display info when running inside a virtual environment"""
    lines = [
        "MATRIX STATUS: Welcome to the construct\n",
        f"Current Python: {sys.executable}",
        f"Virtual Environment: {os.path.basename(sys.prefix)}",
        f"Environment Path: {sys.prefix}\n",
        "SUCCESS: You’re in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.\n",
        "Package installation path:",
        get_packages_loc(),
    ]
    for line in lines:
        print(line)


def main() -> None:
    """Choose the display depending on the environment"""
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
