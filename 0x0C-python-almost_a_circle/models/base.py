#!/usr/bin/python3
""" class Base"""
import json
import csv
import turtle


class Base:
    """ defines base model

    Attributes:
              __nb_objects (int): objects to instantiate
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base objects

        Arguments:
                 id (int): Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Arguments:
                 list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Arguments:
            list_objs (list):  list of instances who inherits of Base
        """
        newfile = cls.__name__ + ".json"
        with open(newfile, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_ = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Arguments:
                json_string (str): string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Arguments:
            **dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_class = cls(1)
            else:
                new_class = cls(1, 1)
            new_class.update(**dictionary)
            return new_class

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_ = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV

        Arguments:
            list_objs (list): List of inherited Base objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): list of rectangles to draw
            list_squares (list): list of squares to draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#32a852")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#4e32a8")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#a8a632")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
