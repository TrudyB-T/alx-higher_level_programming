#!/usr/bin/python3
""" class Base"""


class Base:
    """ defines base model

    Attributes:
              __nb_objects (int): objects to instantiate
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Arguments:
                 id (int): Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
