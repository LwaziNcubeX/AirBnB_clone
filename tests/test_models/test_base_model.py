#!/usr/bin/python3
"""Unittest for BaseModel"""

import datetime
import json
import unittest

from models import storage, FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """
        Test creating a new instance of BaseModel and
        verifying that it has a unique id, created_at and
        updated_at values
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """
        Test updating the updated_at attribute when save()
        method is called.
        """
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict(self):
        """
        Test converting the BaseModel instance to a dictionary with to_dict()
        method and verifying that it has all the keys/values of __dict__,
        __class__ key with class name and created_at and updated_at as strings
        in ISO format.
        """
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIsInstance(d, dict)
        self.assertIn('id', d)
        self.assertIn('created_at', d)
        self.assertIn('updated_at', d)
        self.assertIn('__class__', d)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['created_at'], bm.created_at.isoformat())
        self.assertEqual(d['updated_at'], bm.updated_at.isoformat())

    def test_str(self):
        """
        Test that __str__ method returns the expected string format
        [<class name>] (<self.id>) <self.__dict__> when called on
        the BaseModel instance.
        """
        bm = BaseModel()
        s = str(bm)
        self.assertIn('BaseModel', s)
        self.assertIn(bm.id, s)
        self.assertIn(str(bm.__dict__), s)

    def test_create_from_dict(self):
        """
        Test creating a new BaseModel instance from a dictionary representation
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        new_bm = BaseModel(**bm_dict)
        self.assertIsInstance(new_bm, BaseModel)
        self.assertEqual(new_bm.id, bm.id)
        self.assertEqual(new_bm.created_at, bm.created_at)
        self.assertEqual(new_bm.updated_at, bm.updated_at)

        # Test with additional attributes
        bm.name = "test"
        bm.number = 123
        bm_dict = bm.to_dict()
        new_bm = BaseModel(**bm_dict)
        self.assertEqual(new_bm.__dict__, bm.__dict__)

        # Test with invalid argument
        invalid_dict = {'__class__': 'BaseModel', 'invalid_attr': True}
        with self.assertRaises(TypeError):
            BaseModel(**invalid_dict)
            raise TypeError

    def test_file_storage_save_reload(self):
        """
        Test saving and reloading objects using FileStorage
        """

        bm = BaseModel()
        bm.name = "My_First_Model"
        bm.my_number = 89
        bm.save()

        with open("file.json", "r") as f:
            json_data = json.load(f)
        bm_id = "BaseModel." + bm.id
        self.assertIn(bm_id, json_data)
        self.assertEqual(json_data[bm_id]['name'], bm.name)
        self.assertEqual(json_data[bm_id]['my_number'], bm.my_number)

        # Reload objects from file.json and verify that the object was reloaded
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        all_objs = reloaded_storage.all()
        self.assertIn(bm_id, all_objs)
        reloaded_bm = all_objs[bm_id]
        self.assertEqual(reloaded_bm.id, bm.id)
        self.assertEqual(reloaded_bm.created_at, bm.created_at)
        self.assertEqual(reloaded_bm.updated_at, bm.updated_at)
        self.assertEqual(reloaded_bm.name, bm.name)
        self.assertEqual(reloaded_bm.my_number, bm.my_number)

    def test_link_to_file_storage(self):
        """
        Test linking BaseModel to FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        storage.reload()

        bm = BaseModel()
        bm.save()
        bm_id = "BaseModel." + bm.id
        all_objs = storage.all()
        self.assertIn(bm_id, all_objs)

        with open("file.json", "r") as f:
            json_data = json.load(f)
        self.assertIn(bm_id, json_data)


if __name__ == '__main__':
    unittest.main()
