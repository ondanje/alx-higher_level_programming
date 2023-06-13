#!/usr/bin/python3
"""importing json from standard module"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
