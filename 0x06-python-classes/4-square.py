#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Create a square object"""

    def __init__(self, size=0):
        """Use __init__ to initialize square with private size.
        Args:
             size (int): Private size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square
        Args:
            size (int): size of square
        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """Get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
             size (int): Private size of square.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
