#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """a list of an object's attributes is returned."""
    return (dir(obj))
