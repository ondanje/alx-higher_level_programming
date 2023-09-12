#!/usr/bin/python3
"""
class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """class student """

    def __init__(self, first_name, last_name, age):
        """initialize the instances attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""

        return (self.__dict__.copy())
