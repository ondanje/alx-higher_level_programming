#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
