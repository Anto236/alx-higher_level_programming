#!/usr/bin/python3
"""define a grandchild class which inherits from subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass square which inherits from rectangle"""

    def __init__(self, size):
        """initialize the subclass

        Args:
            square(int): should be an integer > 0
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
