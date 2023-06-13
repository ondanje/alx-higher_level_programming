#!/usr/bin/python3
"""imports json from the standard module"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
