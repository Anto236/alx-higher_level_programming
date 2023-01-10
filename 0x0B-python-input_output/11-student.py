#!/usr/bin/python3

"""Class Student definition"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to retrieve dictionary representation of Student instance"""

        if attrs is None or type(attrs) is not list:
            return (self.__dict__)
        else:
            x = {}
            for y in self.__dict__:
                for z in attrs:
                    if y == z:
                        x[y] = self.__dict__[y]
        return (x)

    def reload_from_json(self, json):
        """Method to replace attributes"""
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
