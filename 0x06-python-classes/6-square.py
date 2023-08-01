#!/usr/bin/python3
"""class square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ passing initial values to object

        Args:
            size (int): size of the square
            position (int, int): position of the new square

        Attributes:
                  __size (int): size of the square
                  position (int, int): position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for n in range(self.__position[0])]
            [print("#", end="") for o in range(self.__size)]
            print()
