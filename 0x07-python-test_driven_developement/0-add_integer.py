#!/usr/bin/python3
"""add_integer method"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float

    Returns:
        The sum of a and b
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
