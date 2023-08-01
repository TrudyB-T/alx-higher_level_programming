#!/usr/bin/python3
"""class square"""


class Square:
    """defines a square"""
    def __init__(self, size):
        """ passing initial values to object

        Args:
            size (int): size of the square

        Attributes:

            __size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
