#!/usr/bin/python3
"""Class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Instantiate a new Student

        Arguments:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Arguments:
        attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Arguments:
        json (dict): The key/value of public attribute
        """
        for j, m in json.items():
            setattr(self, j, m)
