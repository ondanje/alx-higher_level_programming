#!/usr/bin/python3
"""
function that returns the dictionary descriptionwith simple
data structure ; list , dictionary string integer ,boolean
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with
    simple data structure
    """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return (result)
