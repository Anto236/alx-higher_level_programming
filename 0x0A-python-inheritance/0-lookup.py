#!/usr/bin/python3
"""function that returns available attributes and methods of an object"""


def lookup(obj):
    """ function that returns all attributes
        and methods

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
