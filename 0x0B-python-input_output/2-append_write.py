#!/usr/bin/python3

"""Function that appends string at the end of a text file"""


def append_write(filename="", text=""):
    """ Append string to end of a text file
    Args:
        filename (str): name of file to append to
        text (str): string to append to file
    Return: number of characters added
    """

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
