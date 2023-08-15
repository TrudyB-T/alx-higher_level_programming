#!/usr/bin/python3
"""class square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ child class square
    """
    def __init__(self, size):
        """ Initialize square
        """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be greater than 0")
        self.__size = size
