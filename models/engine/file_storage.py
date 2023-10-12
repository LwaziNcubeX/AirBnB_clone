#!/usr/bin/python3
"""A class FileStorage that works with JSON"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
        except FileNotFoundError:
            pass
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                for obj in objects.values():
                    cls_name = obj.pop("__class__")
                    self.new(globals()[cls_name](**obj))
        except FileNotFoundError:
            return
