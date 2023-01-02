#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """Attributes of class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """use __init__ to initialize the attributes
        Args:
            width(int) is 0 if not set
            height(int) is 0 if not set
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            for i in range(self.height):
                rectangle += (self.width * str(self.print_symbol)) + "\n"
            return rectangle[:-1]

    def __repr__(self):
        """method returning string representation of instance"""

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """method called when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new recatangle instance
        width == height == size
        """

        return cls(size, size)
