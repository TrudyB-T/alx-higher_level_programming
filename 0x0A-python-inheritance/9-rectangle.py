#!/usr/bin/python3
"""class rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ child class inheriting from basegeometry
    """
    def __init__(self, width, height):
        """ Initialize rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns a string form of rectangle
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """returns the rectangle area
        """
        return self.__width * self.__height
