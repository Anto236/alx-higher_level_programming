#!/usr/bin/python3
"""function that returns True/False if obj is an instance of a class"""


def inherits_from(obj, a_class):
    """function does as described

    Args:
        obj: object to check
        a_class: class to check against
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
