#!/usr/bin/python3

"""Function that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Create json representation of string opbject
    Args: my_obj (str): object to make json representation of
    Return: JSON representation of object
    """
    return (json.dumps(my_obj))
