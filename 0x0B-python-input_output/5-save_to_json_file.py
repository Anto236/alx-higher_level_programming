#!/usr/bin/python3

"""Function that writes object to txt file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write obj to txt file using json
    Args:
        my_obj (obj): object to rwite to file
        filename (str): file to write to
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
