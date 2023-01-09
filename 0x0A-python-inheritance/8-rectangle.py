#!/usr/bin/python3
"""defining a subclass Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method to initialize
        Args:
            width(int): must be an integer
            height(int): must be an integer
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
