"""Demonstrates Counter() for counting repeated items."""

from collections import Counter


def count_items():
    """Return the frequency of each item in a list."""

    items = ["Python", "SQL", "Python", "Excel", "SQL", "Python"]

    return Counter(items)