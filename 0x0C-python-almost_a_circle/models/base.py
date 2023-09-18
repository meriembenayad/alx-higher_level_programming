#!/usr/bin/python3
"""class base"""
import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__+".json"
        with open(filename, 'w', encoding="utf-8") as filejson:
            list_dict = []
            if list_objs is None or len(list_objs) == 0:
                json.dump(json.loads(cls.to_json_string(list_dict)), filejson)
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                json.dump(json.loads(cls.to_json_string(list_dict)), filejson)

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
        """save ti file csv"""
        import csv

        filename = cls.__name__ + '.csv'
        try:
            listcsv = [obj.to_dictionary() for obj in list_objs]
        except FileNotFoundError:
            listcsv = '[]'
        keys = listcsv[0].keys()
        with open(filename, mode='w', encoding="utf-8") as filecsv:
            writer = listcsv.DictWriter(filecsv, keys)
            writer.writeheader()
            writer.writerows(listcsv)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        import csv
        filename = cls.__name__ + '.csv'
        if not os.path.isfile(filename):
            return []

        listcsv = []
        with open(filename, mode='r', encoding="utf-8") as filecsv:
            reader = listcsv.DictReader(filecsv)

            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except ValueError:
                        pass
                listcsv.append(row)
        return [cls.create(**dic) for dic in listcsv]
