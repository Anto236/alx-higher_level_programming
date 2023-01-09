#!/usr/bin/python3

"""subclass that inherits from int"""


class MyInt(int):
    """MyInt subclass of int"""

    def __eq__(self, other):
        """opposite of =="""

        return (super().__ne__(other))

    def __ne__(self, other):
        """opposite of !="""
        return (super().__eq__(other))

