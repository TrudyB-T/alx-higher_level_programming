#!/usr/bin/python3
"""Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize class

        Arguments:
                size (int): Square size
                x (int): x coordinate
                y (int): y coordinate
                id (int): Square identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/Get Square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square

        Arguments:
                *args (ints): new attribute
                - 1st argument: id attribute
                - 2nd argument: size attribute
                - 3rd argument: x attribute
                - 4th argument: y attribute
                **kwargs (dict): key-value pairs of attributes.
        """
        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size> - width or height"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
