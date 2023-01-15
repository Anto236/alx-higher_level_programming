#!/usr/bin/python3
"""define a class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """instantation of class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to retrieve attributes
        create a variable to store attributes
        """

        student_dict = {}
        """check if attrs exist"""
        if attrs:
            """loop through and add the attrs"""
            for attr in attrs:
                """use method hasatt to check if attr exist
                if true use method getattr to get attrs
                """
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            else:
                student_attr = self.__dict__

            return(student_dict)
