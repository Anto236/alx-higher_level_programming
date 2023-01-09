#!/usr/bin/python3
def lookup(obj):
    """ function that returns all attributes
        and methods

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
