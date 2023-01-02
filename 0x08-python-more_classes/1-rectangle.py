#!/usr/bin/python3
"""create a class rectangle"""


class Rectangle:
    """define an object class"""

    def __init__(self, width=0, height=0):
        """Use __init__ to initialize
        Args: width(int) height(int)
        """

        self.__width = width
        self.__height = height

    @property
    def height(self):
        """get the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height
        Args: height(int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width
        Args: width(int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
