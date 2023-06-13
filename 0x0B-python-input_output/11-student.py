#!/usr/bin/python3
"""
class Student that defines a student by(based on 10-student.py):
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

        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):

            result = self.__dict__.copy()
        else:

            result = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return (result)

    def reload_from_json(self, json):
        """ replaces attributes of the class Student instance """

        for i in json:
            self.__dict__[i] = json[i]
