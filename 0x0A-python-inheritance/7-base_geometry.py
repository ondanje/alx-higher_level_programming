#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """class BaseGeometry"""

    def area(self):
        """area method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate values"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
