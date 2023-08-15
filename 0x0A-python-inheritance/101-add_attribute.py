#!/usr/bin/python3
""" adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """ adds a new attribute to an object
    """
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[name] = value
