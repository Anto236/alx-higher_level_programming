#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and then save them to a
file
"""
import sys
import os
import json

"""use required functions """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""create an empty list to store arguments"""
args_list = []

"""check if the list exists"""
file_name = "add_item.json"
if os.path.isfile(file_name):
    """load the list from the json file if it exists"""
    args_list = load_from_json_file(file_name)

"""iterate through the command line arguments and add on them"""
for arg in sys.argv[1:]:
    args_list.append(arg)

"""save the list to a json file"""
save_to_json_file(args_list, file_name)
