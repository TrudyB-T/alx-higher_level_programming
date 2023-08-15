#!/usr/bin/python3
"""
    class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    child class that inherits fromparent class BaseGeometry
    """
    def __init__(self, width, height):
        """
            Instantiate rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
