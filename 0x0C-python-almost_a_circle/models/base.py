#!/usr/bin/python3
"""class base"""
import json
import csv
import turtle


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__+".json"
        with open(filename, mode="w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        if cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__ + '.json')
        try:
            with open(filename, mode="r") as filejson:
                new_list = []
                list_dicts = cls.from_json_string(
                    json.dumps(json.load(filejson)))
                for di in list_dicts:
                    new_list.append(cls.create(**di))
                return new_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save file csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as filecsv:
            if list_objs is None or list_objs == []:
                filecsv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(filecsv, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as filecsv:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(filecsv, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares."""
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Turtle Drawing")

        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("gold")
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("silver")
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.exitonclick()
