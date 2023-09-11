#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """initialize the instances of the class :width and height """

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """method to calculate the area of a rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """__str__ method for return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
