#!/usr/bin/python3
"""
Defining a class square that inherits from base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from the Rectangle class
    Methods:
            __init__()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ : constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            return a string representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
            return the size(width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter function
            Args:
                value (int): set size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

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
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
            return dict representation of Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def to_dictionary(self):
        """
            return dict representation of Square instance
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
