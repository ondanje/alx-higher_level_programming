#!/usr/bin/python3
"""print square with # characters"""


def print_square(size):
    """print square function

    args:
    size: length of the square
    return:
    a square drawn using # characters
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for index in range(size):
        print("#" * size)
