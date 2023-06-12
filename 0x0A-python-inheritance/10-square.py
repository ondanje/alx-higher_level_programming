#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class Square that inherits from Rectangle (9-rectangle.py):"""


class Square(Rectangle):
    """class square"""

    def __init__(self, size):

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area"""

        return self.__size * self.__size
