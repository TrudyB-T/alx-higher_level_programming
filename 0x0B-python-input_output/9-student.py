#!/usr/bin/python3
"""Class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Instantiate a new Student.
        
        Arguments:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation
        of a Student instance"""
        return self.__dict__
