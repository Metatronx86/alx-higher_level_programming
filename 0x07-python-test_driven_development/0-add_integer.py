#!/usr/bin/python3
"""Defines an integer summation function."""


def add_integer(a, b=98):
    """Calculate the integer sum of a and b.

    Floating-point arguments are typecasted to integers before the summation is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-floating-point value.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

