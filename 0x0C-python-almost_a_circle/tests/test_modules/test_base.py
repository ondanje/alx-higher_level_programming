#!/usr/bin/python3
"""importing modules for testing the base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base_Create(unittest.TestCase):
    """class test of the create base function"""

    def test_rectangle_create(self):
        """test rectangle creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
