#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Create a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """Use __init__ to initialize square with private size.
        Args:
             size (int): Private size of square.
             position (tuple): Position of square
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """Print square to stdout using #
        Args:
             square (str): used to print square
        """
        tup1 = self.__position[0] * " "
        tup2 = self.__position[1] * "\n"

        if self.size == 0:
            print()
            return
        if self.__position[1] > 0:
            print(tup2, end="")
        for x in range(self.size):
            square = self.size * "#"
            print(tup1, end="")
            print(square)

    @property
    def position(self):
        """Get the designated position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position"""

        if (isinstance(value, tuple) is False or
                len(value) != 2 or
                isinstance(value[0], int) is False or
                isinstance(value[1], int) is False or
                value[0] < 0 or value[1] < 0):

            raise TypeError("position must be a tuple of 2 positive integers")
            return

        self.__position = value
