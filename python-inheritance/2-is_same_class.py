#!/usr/bin/python3
""" 2. Exact same object Python - Inheritance, """


def is_same_class(obj, a_class):
    """Tests if an object is exactly an instance of a specific class.

    Args:
        obj (any): object of any type
        a_class (class): class to test against

    Returns:
        True if obj is an instance of a_class, False otherwise.

    """
    return (type(obj) == a_class)
