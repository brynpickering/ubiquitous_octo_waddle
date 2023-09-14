"""Main module."""
from pathlib import Path


def my_path(extra: str):
    """My path

    Args:
        extra (str): extra to add to print
    """
    print(Path(__file__), extra)
