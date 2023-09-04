#!/usr/bin/python3
"""Defines a function add_integer(a, b=98) that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers or float
    args:
    a: first value
    b: second value

    raises:
    TypeError: if argument is not float or integer
    return:
    sum of the 2 numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
