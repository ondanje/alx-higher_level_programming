#!/usr/bin/python3
"""class Square that defines a square based on 2-square.py"""


class Square:
    """a square"""

    def __init__(self, size=0):
        """initialize a square

        Args:
            size(int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of the square"""
        return (self.__size*self.__size)
