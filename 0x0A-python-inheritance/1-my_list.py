#!/usr/bin/python3
"""
 class MyList
"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
