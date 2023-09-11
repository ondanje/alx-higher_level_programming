#!/usr/bin/python3
"""
class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area"""

        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
