#!/usr/bin/python3

"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Write string to a text file
    Args:
        filename (str): filename to write to
        text (str): string to write to file
    Return: Number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
