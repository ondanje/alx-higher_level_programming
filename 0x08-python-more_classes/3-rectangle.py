#!/usr/bin/python3
"""class Rectangle that defines a rectangle based on 2-rectangle.py"""


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle

        Returns
        area(int): height * width
        """

        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle

        Returns
        perimeter(int): 2(height * width)
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def draw_rectangle(self):
        """prints a string of '#' characters to form a  rectangle

        Property:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle
            drawing (str): string to constructed for return

        Returns:
            drawing (str): draawing using #
        """

        drawing = ""
        for row in range(self.__height):
            for col in range(self.__width):
                drawing += '#'
            if self.__width != 0 and row < (self.__height - 1):
                drawing += '\n'
        return drawing

    def __str__(self):
        """Allows direct printing of instances.

        Returns:
            The output of draw_rectangle method

        """
        return self.draw_rectangle()
