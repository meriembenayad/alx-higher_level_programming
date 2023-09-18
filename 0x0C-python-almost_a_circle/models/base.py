#!/usr/bin/python3
""" Base class """
import json


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as filejson:
            if list_objs is None:
                filejson.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                filejson.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as filejson:
                listjson = cls.from_json_string(filejson.read())
            for i, j in enumerate(list):
                listjson[i] = cls.create(**listjson[i])
            return listjson
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        filename = cls.__name__ + ".csv"
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(i.to_dictionary())
        list = cls.to_json_string(list)
        with open(filename, mode="w", encoding="utf-8") as filecsv:
            filecsv.write(list)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as filecsv:
                listcsv = cls.from_json_string(filecsv.read())
            for i, j in enumerate(listcsv):
                listcsv[i] = cls.create(**listcsv[i])
            return listcsv
        except FileNotFoundError:
            return []
