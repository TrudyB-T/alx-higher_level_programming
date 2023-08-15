#!/usr/bin/python3
"""class MyInt
"""


class MyInt(int):
    """ MyInt has == and != operators inverted.
    """
    def __eq__(self, value):
        """ invert ==
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ invert !=
        """
        return super().__eq__(value)
