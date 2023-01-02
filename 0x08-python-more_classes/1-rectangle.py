#!/usr/bin/python3
"""a class rectangle that gets the height and width of a rectangle
"""


class Rectangle:
    """
    a class that gets the width and height of rectanle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        @value - receives the value of height
        """
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        @value - receives the value of width
        """
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
