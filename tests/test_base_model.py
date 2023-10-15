#!/usr/bin/python3
"""Unittest for BaseModel"""

import datetime
import unittest
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


if __name__ == '__main__':
    unittest.main()
