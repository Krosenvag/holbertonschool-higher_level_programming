#!/usr/bin/python3
"""Custom list type intended to only contain integers.
"""


class MyList(list):
    """Custom list type intended to only contain integers.
    """
    def print_sorted(self):
        """Prints MyList lists in ascending order by value.
        """
        print(sorted(self))
