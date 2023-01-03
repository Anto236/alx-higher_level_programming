#!/usr/bin/python3
""" this is a module that has a class that avoids
dynamically creating attributes
"""


class LockedClass:
    __slots__ = "first_name"
    
    pass

