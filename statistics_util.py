"""Demonstrates statistics.mean() for calculating the average of numbers."""

import statistics


def calculate_average():
    """Return the average of a list of marks."""

    marks = [80, 85, 90, 75, 95]

    return statistics.mean(marks)