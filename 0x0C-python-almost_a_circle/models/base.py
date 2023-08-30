#!/usr/bin/python3
"""Base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a json object to a json string"""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves objects to a file"""
        dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts json strings to json objects"""
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a class"""
        if cls.__name__ == 'Rectangle':
            dum = cls(1, 2)
        else:
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """Loads instances on an object from a file"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                read = f.read()
        except FileNotFoundError:
            return []
        read = cls.from_json_string(read)
        instances = []
        for inst_dict in read:
            instances.append(cls.create(**inst_dict))
        return instances
