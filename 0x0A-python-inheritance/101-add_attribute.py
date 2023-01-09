#!/usr/bin/python3
"""function that adds attribute to object"""


def add_attribute(obj, attr, value):
    """Function to add attribute

    Args:
        obj: object to aadd attribute to
        attr: name to add
        value: attribute value to set value
    """

    if hasattr(obj, "__dict__"):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
