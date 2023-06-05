#!/usr/bin/python3
"""class Rectangle that defines a rectangle based on 8-rectangle.py"""


class Rectangle:
    """class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
                drawing += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                drawing += '\n'
        return drawing

    def __str__(self):
        """Allows direct printing of instances.

        Returns:
            The output of draw_rectangle method

        """
        return self.draw_rectangle()

    def __repr__(self):
        """Allows use of the func eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def __del__():
        """Print this message upon deletion of the object/instance.
        decrementss the number of instances

        """
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides = square
        """
        return cls(size, size)
