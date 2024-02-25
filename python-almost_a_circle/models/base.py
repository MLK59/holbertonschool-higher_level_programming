#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """
    Represent the base model for all other classes in project 0x0C*
    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base

        Args:
            id(int): the identity of a new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation to a file

        Args:
            list_objs (list): A list of instances
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Loads an instance with a dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file
        """
        from os import path

        filename = f"{cls.__name__}.json"
        if not path.isfile(filename):
            return []
        with open(filename, "r") as f:
            list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves objects to a CSV file
        """
        import csv
        from models.rectangle import Rectangle
        from models.square import Square

        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is not None:
                if cls is Rectangle:
                    rows = [
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs
                    ]
                elif cls is Square:
                    rows = [[obj.id, obj.size, obj.x, obj.y]
                            for obj in list_objs]
                else:
                    rows = []
                writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """
        Retrieves objects from a CSV file
        """
        import csv
        from models.rectangle import Rectangle
        from models.square import Square

        filename = f"{cls.__name__}.csv"
        load = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {
                        "id": row[0],
                        "width": row[1],
                        "height": row[2],
                        "x": row[3],
                        "y": row[4],
                    }
                elif cls is Square:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                else:
                    d = {}
                load.append(cls.create(**d))
        return load
