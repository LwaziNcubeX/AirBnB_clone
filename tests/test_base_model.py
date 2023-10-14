#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def test_id_is_str(self):
        """Test id attribute is a string"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_created_at_is_datetime(self):
        """Test created_at attribute is a datetime object"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at attribute is a datetime object"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that calling save method updates updated_at attribute"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict method returns a dictionary"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that keys in to_dict dictionary are correct"""
        my_model = BaseModel()
        dict_keys = my_model.to_dict().keys()
        expected_keys = {'id', 'created_at', 'updated_at', '__class__'}
        self.assertEqual(set(dict_keys), expected_keys)

    def test_to_dict_contains_correct_types_and_values(self):
        """Test that types and values in to_dict dictionary are correct"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()

        # Test that keys have correct value types
        self.assertIsInstance(my_model_dict['id'], str)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertIsInstance(my_model_dict['__class__'], str)

        # Test that datetime values can be parsed
        datetime.strptime(my_model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        datetime.strptime(my_model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def test_init_with_valid_kwargs(self):
        """Test initializing BaseModel with valid kwargs"""
        valid_kwargs = {'id': '123', 'created_at': '2022-01-01T00:00:00',
                        'updated_at': '2022-01-02T00:00:00'}
        my_model = BaseModel(**valid_kwargs)
        self.assertEqual(my_model.id, valid_kwargs['id'])
        self.assertEqual(my_model.created_at.isoformat(),
                         valid_kwargs['created_at'])
        self.assertEqual(my_model.updated_at.isoformat(),
                         valid_kwargs['updated_at'])

    def test_init_with_invalid_kwargs(self):
        """Test initializing BaseModel with invalid kwargs"""
        invalid_kwargs = {'id': '123', 'created_at': '2022-01-01T00:00:00.000000',
                          'updated_at': '2022-01-02T00:00:00.000000', 'invalid_key': 'value'}
        BaseModel(**invalid_kwargs)
        with self.assertRaises(AttributeError):
            raise AttributeError

    def test_init(self):
        """Test creating a new BaseModel instance"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test __str__ method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), '[BaseModel] ({}) {}'.format(my_model.id, my_model.__dict__))

    def test_save(self):
        """Test save method of BaseModel"""
        my_model = BaseModel()
        updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)
        self.assertIn('name', my_model_json)
        self.assertIn('my_number', my_model_json)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)


if __name__ == '__main__':
    unittest.main()
