#!/usr/bin/python3
"""

prints a square with the character #

"""


def print_square(size):
    """prints a square with the character #

    Arguments:
             size: square size


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for m in range(size):
        print("#" * size)
