#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0):
        """initialize squa
        Args:
            size (int): size of the square"""
        self.__size = size  #: size of the square
        if ((isinstance(size, int)) is True):
            pass
        if ((isinstance(size, int)) is not True):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
