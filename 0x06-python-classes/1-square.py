#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Create a square object"""

    def __init__(self, size=None):
        """Use __init__ to initialize square with private size
        Args:
             size (int): Private size of square
        """

        self.__size = size
