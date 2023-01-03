#!/usr/bin/python3
"""
addition of two integers
checkes for integers
checks for floats
"""


def add_integer(a, b=98):
    """
    a function that adds two integers
    @a: number one
    @b: number two
    """
    if isinstance(a, int):
        pass
    elif isinstance(a, float):
        a = int(a)
        pass
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int):
        return a + b
    elif isinstance(b, float):
        b = int(b)
        return a + b
    else:
        raise TypeError("b must be an integer")
