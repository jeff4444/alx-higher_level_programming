#!/usr/bin/python3
"""
This is the "add_integer" module.
"""

def add_integer(a, b=98):
    """Return the sum of a and b
    """

    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError('a must be an integer')
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError('b must be an integer')
    return int(a) + int(b)
