#!/usr/bin/python3
"""A class FileStorage that works with JSON"""
import json

from models.base_model import BaseModel


class FileStorage(BaseModel):
    __file_path = 'file.json'
    __objects = {}
    id = 12121212

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump([obj.to_dict() for obj in self.__objects.values()], f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for obj in objects:
                    cls_name = obj.pop('__class__')
                    cls = globals()[cls_name]
                    key = "{}.{}".format(cls_name, obj['id'])
                    self.__objects[key] = cls(**obj)
        except FileNotFoundError:
            pass
