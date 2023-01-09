#!/usr/bin/python3
"""module to check  if og=bject is an instance"""


def is_kind_of_class(obj, a_class):
    """ function to check if object is an instance
        of a class that inherited from specified class
   
    Args:
        obj: object to to checked
        a_class: class to compare with

    Return: True otherwise False
    """

    return True if isinstance(obj, a_class) else False
