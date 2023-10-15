#!/usr/bin/python3
"""A class FileStorage that works with JSON"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


CLASSES = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """
    The FileStorage class provides a way to store and retrieve data
    from a file.

    Attributes:
        __file_path (str): The name of the file to store the data in.
        __objects (dict): An empty dictionary to store all objects

    Methods:
        all(self):
            returns the dictionary __objects
        new(self, obj):
            sets in __objects the obj with key <obj class name>.id
        save(self):
            serializes __objects to the JSON file (path: __file_path)
        reload(self):
            deserializes the JSON file to __objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects

        param arg:
        return:
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        param arg:
        return:
        """
        if isinstance(obj, dict) and "__class__" in obj:
            cls_name = obj.pop("__class__")
            cls = eval(cls_name)
            self.__objects[obj["id"]] = cls(**obj)
        else:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)

        param arg:
        return:
        """
        obj_dict = self.__objects
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
        except FileNotFoundError:
            pass
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists otherwise, do nothing.

        param arg:
        return:
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                for obj in objects.values():
                    cls_name = obj.pop("__class__")
                    if cls_name in CLASSES:
                        obj = CLASSES[cls_name](**obj)
                    else:
                        obj = globals()[cls_name](**obj)
                    self.new(obj)
        except FileNotFoundError:
            pass
