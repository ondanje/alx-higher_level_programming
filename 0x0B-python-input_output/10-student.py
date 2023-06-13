#!/usr/bin/python3
"""
class Student that defines a student by(based on 9-student.py):
Public instance attributes:first_name,last_name
age
"""


class Student:
    """class student """

    def __init__(self, first_name, last_name, age):
        """initialize the instances attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return (self.__dict__)
