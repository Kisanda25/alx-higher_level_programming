#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """Adds an attribute to an object if possible.

    Args:
        obj (any): The object to add .
        att (str): The name of the attribute.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
