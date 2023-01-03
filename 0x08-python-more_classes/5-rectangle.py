#!/usr/bin/python3
"""a class rectangle that gets the height and width of a rectangle
"""


class Rectangle:
    """
    a class that gets the width and height of rectanle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):

        """
        returns the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            area = self.__width * self.__height
            for i in range(area):
                if (i % self.__width == 0) and i != 0:
                    print()
                print("#", end="")
            return ""
        else:
            return str()

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print(f"Bye rectangle...")
