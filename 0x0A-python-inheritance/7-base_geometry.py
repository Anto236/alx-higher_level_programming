#!/usr/bin/python3

"""Define class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class methods and attributes"""

    def area(self):
        """Currently unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value
        Args:
            name (str): name of value
            value (int): value to validate
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
