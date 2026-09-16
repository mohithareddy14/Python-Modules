"""Demonstrates re.findall() for finding all numbers in text."""

import re


def find_numbers():
    """Return all numbers found in a sample text."""
    text = "Python 3 is popular and SQL 2 is also useful."

    return re.findall(r"\d+", text)