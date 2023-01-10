#!/usr/bin/python3

""" Function that returns Python object from JSON string"""
import json


def from_json_string(my_str):
    """Return pyhon obj from json str"""

    return (json.loads(my_str))
