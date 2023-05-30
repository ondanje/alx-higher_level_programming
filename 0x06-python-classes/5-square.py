#!/usr/bin/python3
"""class Square that defines a square based on 4-square.py"""


class Square:
    """a square"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """retrieve current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square using the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
