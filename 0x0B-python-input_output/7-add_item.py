#!/usr/bin/python3

"""Script that adds all arguments to a python list and then saves to a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function to execute script"""

    try:
        args = load_from_json_file("add_item.json")
    except:
        args = []

    args.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")


if __name__ == "__main__":
    main()
