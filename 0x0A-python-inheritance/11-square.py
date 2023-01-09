#!/usr/bin/python3
"""module that inherits from a superclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a grandchild class"""

    def __init__(self, size):
        """initialize the subclass

        Args:
            size(int): should be an integer > 0
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns square with description
        [Square] <width>/<height>
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
