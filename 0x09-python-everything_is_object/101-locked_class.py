#!/usr/bin/python3
"""Locked class only containing attribute first_name"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """use __Init__"""
        pass
