#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function add_integer takes two arguments and returns their sum.
If one of the arguments is a float, it is cast to an integer.
If the arguments are not numbers, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats, cast to integers if needed.

    Args:
        a: first number (int or float)
        b: second number (int or float), default is 98

    Returns:
        The sum of a and b after casting to integers

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)