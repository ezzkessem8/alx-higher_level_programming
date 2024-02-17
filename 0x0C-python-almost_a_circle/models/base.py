#!/usr/bin/python3
"""Module defining Base class."""

import json


class Base:
    """Base class for other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base object with optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to file."""
        filename = cls.__name__ + ".json"
        objs = []
        if list_objs:
            objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance with attributes from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load list of instances from file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

