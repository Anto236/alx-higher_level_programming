#!/usr/bin/python3
"""define a Rectangle sub-class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define a subclass from the Parent BaseGeometry"""

    def __init__(self, width, height):
        """initialize the subclass

        Args:
            width(int): should be an integer and > 0
            height(int): should be an integer and > 0
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method to calculate the area"""

        return (self.__width * self.__height)

    def __str__(self):
        """method to return rectangle description"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
