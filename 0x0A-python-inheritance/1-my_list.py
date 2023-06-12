#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """class inheriting from a list class"""

    def print_sorted(self):
        """method to sort a list"""

        return (sorted(list(self)))
