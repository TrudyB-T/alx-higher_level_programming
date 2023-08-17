#!/usr/bin/python3
"""
class JSON
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string,
    integer and boolean) for JSON serialization of an object"""

    attribute = {}
    if hasattr(obj, "__dict__"):
        attribute = obj.__dict__.copy()
    return attribute
