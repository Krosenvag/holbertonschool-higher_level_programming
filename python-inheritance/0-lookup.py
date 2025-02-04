#!/usr/bin/python3
""" Python - Inheritance, task 0 """


def lookup(obj):
    """Returns the list of available attributes and methods of an object.
    Args:
        obj (any): object of any type
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
