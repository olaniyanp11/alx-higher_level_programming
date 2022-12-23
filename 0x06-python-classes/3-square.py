#!/usr/bin/python3
"""Square that defines a square """


class Square:
    """a class called Square was created"""

    def __init__(self, size=0):
        """ Args:
            self == instance
            size = size of the squares
        """
        self.__size = size  #: size of the square
        if ((isinstance(size, int)) is True):
            pass
        if ((isinstance(size, int)) is not True):
            raise TypeError("size must be an integer")
        if size < 0:                     
            raise ValueError("size must be >= 0")
    def area(self):
        """
        Args:
             self :
                create an instance
             Return : 
                the current area of the  square
        """
        if self.__size == 0:
            return self.__size
        else:
            return self.__size ** 2
