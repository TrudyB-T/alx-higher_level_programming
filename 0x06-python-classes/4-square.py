#!/usr/bin/python3
"""class square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """ passing initial values to object

        Args:
            size (int): size of the square

        Attributes:

            __size (int): size of the square
        """
        self.size = size

    @property 
    def size(self):
        """ retrieve private instance attribute: size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
