#!/usr/bin/python3
"""module to check type"""


def is_same_class(obj, a_class):
    """check if function is exactly an instance
        in specified class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        true is it is specified otherwise False
    """

    return True if type(obj) is a_class else False
