#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """Attributes of class rectangle"""

    def __init__(self, width=0, height=0):
        """use __init__ to initialize the attributes
        Args:
            width(int) is 0 if not set
            height(int) is 0 if not set
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width
        Args: width(int)
        """

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height
        Args: width(int)
        """

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """finds the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """finds perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ method that returns rectangle #
        """

        if self.__width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            for row in range(self.height):
                for column in range(self.width):
                    rectangle += "#"
                if row == self.height - 1:
                    break
                else:
                    rectangle += "\n"
            return rectangle
