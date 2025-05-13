#!/usr/bin/python3
"""
This module contains the function add_integer.
It adds two integers or floats, and returns an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a: First number (int or float).
        b: Second number (int or float, default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)