#!/usr/bin/python3

"""Function that reads and then prints a txt file to stdout"""


def read_file(filename=""):
    """Read from file then printk"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
