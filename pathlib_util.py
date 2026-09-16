"""Demonstrates pathlib.Path.exists() for checking whether a path exists."""

from pathlib import Path


def check_file_exists():
    """Check whether the current Python file exists."""

    file_path = Path(__file__)

    return file_path.exists()