#!/usr/bin/python3
"""A module that inherits from a list"""


class MyList(list):
    """Class that inherits from a list"""

    def print_sorted(self):
        """ sorts a list
        """

        print(sorted(self))
