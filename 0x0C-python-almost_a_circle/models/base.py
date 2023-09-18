#!/usr/bin/python3
import json
import os
import csv
import ast


class Base:
    """ Base class for other classes in the project """
    """ A private class attribute to count the number of objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a Base instance with an id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        """ Create the filename """
        filename = cls.__name__ + ".json"

        """ Open the file in write mode """
        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            list_dicts = [obj.to_dictionary() for obj in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Return list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set
            Create dummy instance with dummy mandatory attributes
            Access the class name & create the instance
            Check if class is Rectangle or Square
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Returns list of instances from a file.
            Create a filename.
            Check if the file exists by using os module:
                - if doesn't exist: return an empty list.
                - if does exist: open the file in read mode.
            Call the from_json_string method to convert the JSON string
            to a list of dictionary.
            Create a list of instances using the create method
            and each dictionary in the list
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as filejson:
            json_string = filejson.read()
            list_dicts = cls.from_json_string(json_string)
            list_instances = [cls.create(**inst) for inst in list_dicts]
            return list_instances

    """ Advanced Tasks """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Write the CSV representation of list_objs to a file
            Create a file by using cls parameter
            Open the file in write mode:
                - Create a writer object by using csv module
                - Convert each object to a dictionary,
                by using to_dictionary method
                - Check if class Rectangle or Square:
                    - Create a list of values in the order of id, width, height, x, y
                    - create a list of values in the order of id, size, x, y
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8") as filecsv:
            writer = csv.writer(filecsv)
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                if cls.__name__ == "Rectangle":
                    row = [obj_dict["id"], [obj_dict["width"],
                                            obj_dict["height"], obj_dict["x"], obj_dict["y"]]]

                if cls.__name__ == "Square":
                    row = [obj_dict["id"], obj_dict["size"],
                           obj_dict["x"], obj_dict["y"]]

                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
            Retrun a list of instances from a file
            Create a file by using cls module
            Empty list to store the instances
            Open the file in read mode
                - Create a reader obj using csv module
                - Loop to iterate over rows in the file
        """
        filename = cls.__name__ + ".csv"
        list_instances = []
        with open(filename, mode="r", encoding="utf-8") as filecsv:
            reader = csv.reader(filecsv)
            for row in reader:
                row_list = ast.literal_eval(row[1])
                if cls.__name__ == "Rectangle":
                    obj_dict = {"id": int(row[0]), "width": row_list[0],
                                "height": row_list[1], "x": row_list[2], "y": row_list[3]}

                if cls.__name__ == "Square":
                    obj_dict = {"id": int(row[0]), "size": row_list[0],
                                "x": row_list[1], "y": row_list[2]}

                list_instances.append(cls.create(**obj_dict))
            return list_instances
