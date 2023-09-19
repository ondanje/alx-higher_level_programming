#!/usr/bin/python3
"""
Defining a class rectangle that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle that inherits from the Base class
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            __INIT__ A CLASS INSTANCE
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            function getter
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
           setter function
           Args:
                value (int): set value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            function getter
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
           setter function
           Args:
                value (int): set value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            function getter
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
           setter function
           Args:
                value (int): set x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            function getter
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
           setter function
           Args:
                value (int): set y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns area of rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            print a rectangle using #
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print('' * self.__x + "#" * self.__width)

    def __str__(self):
        """
            return a string representation
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        """
            assigns values to attributes
            Args:
                *args: variable
                **kwargs - kwrgs
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """
            return dict
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
