import os
import site
import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_packages_path() -> str:
    paths = site.getsitepackages()
    if paths:
        return paths[0]
    return "Unknown"


def show_outside_venv() -> None:
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
    lines = [
        "MATRIX STATUS: Welcome to the construct\n",
        f"Current Python: {sys.executable}",
        f"Virtual Environment: {os.path.basename(sys.prefix)}",
        f"Environment Path: {sys.prefix}\n",
        "SUCCESS: You’re in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.\n",
        "Package installation path:",
        get_packages_path(),
    ]
    for line in lines:
        print(line)


def main() -> None:
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
