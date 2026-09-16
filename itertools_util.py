"""Demonstrates itertools.chain() for combining multiple iterables."""

from itertools import chain


def combine_lists():
    """Combine two lists into a single list."""

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    return list(chain(list1, list2))