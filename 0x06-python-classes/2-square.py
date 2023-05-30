#!/usr/bin/python3
"""class Square that defines a square based on 1-square.py"""


class Square:
    """A square"""

    def __init__(self, size=0):
        """initialize the square

        Args:
        size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
