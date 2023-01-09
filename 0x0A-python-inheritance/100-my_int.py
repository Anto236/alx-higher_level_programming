#!/usr/bin/python3

"""Subclass MyInt that inherits from int"""


class MyInt(int):
    """MyInt subclass of int"""

    def __eq__(self, other):
        """Opposite of equal"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """Opposite of not equal"""
        return (super().__eq__(other))
