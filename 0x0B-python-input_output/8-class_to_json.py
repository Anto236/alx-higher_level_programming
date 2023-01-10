#!/usr/bin/python3

"""Returns dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns dicitonary description for JSON serialization"""
    return (obj.__dict__)
