#!/usr/bin/python3
"""A class FileStorage that works with JSON"""
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = FileStorage.__objects
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
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                for obj in objects:
                    if isinstance(obj, dict):
                        cls_name = obj.pop('__class__')
                        cls = globals()[cls_name]
                        key = "{}.{}".format(cls_name, obj['id'])
                        self.__objects[key] = cls(**obj)
        except FileNotFoundError:
            pass
