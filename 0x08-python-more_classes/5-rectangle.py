#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """ defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ passing initial values to object

           Args:
               width (int): width of the rectangle
               height (int): height of the rectangle

           Attributes:
                     width (int): width of the rectangle
                     height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimiter of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for m in range(self.__width)])
                for n in range(self.__height)]))

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print the message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
