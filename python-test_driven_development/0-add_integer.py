#!/usr/bin/python3
"""A module to add two integers.

This module provides a function to add two integers or floats.
Both arguments are cast to integers before addition.
No external modules are imported.

"""


def add_integer(a, b=98):
    """Add two integers or floats.

    Both arguments are cast to integers before addition.
    Returns the sum as an integer.

    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.

    Returns:
        int: The result of the addition.

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
