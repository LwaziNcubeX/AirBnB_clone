#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up a new instance of FileStorage for each test case.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Remove the JSON file created by the tests.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_FileStorage_instance(self):
        """
        Test that self.storage is an instance of FileStorage.
        """
        self.assertIsInstance(self.storage, FileStorage)

    def test_Objects_dict(self):
        """
        Test that self.storage.__objects is a dictionary.
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_FilePath_str(self):
        """
        Test that self.storage.__file_path is a string.
        """
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_all(self):
        """
        Test that self.storage.all() returns a dictionary.
        """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """
        Test that self.storage.new(obj) adds the object to __objects.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.assertIn("BaseModel.{}".format(bm1.id), self.storage.all().keys())
        self.assertIn(bm1, self.storage.all().values())

        self.storage.new(bm2)
        self.assertIn("BaseModel.{}".format(bm2.id), self.storage.all().keys())
        self.assertIn(bm2, self.storage.all().values())

    def test_save(self):
        """
        Test that self.storage.save() writes the objects to the JSON file.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as f:
            file_dict = json.load(f)

        self.assertIn("BaseModel.{}".format(bm1.id), file_dict)
        self.assertTrue(all(key in file_dict["BaseModel.{}".format(bm1.id)]
                        for key in ["id", "created_at",
                                    "updated_at", "__class__"]))
        self.assertIn("BaseModel.{}".format(bm2.id), file_dict)
        self.assertTrue(all(key in file_dict["BaseModel.{}".format(bm2.id)]
                        for key in ["id", "created_at",
                                    "updated_at", "__class__"]))

    def test_reload(self):
        """
        Test that self.storage.reload() loads objects from the JSON file.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        storage2 = FileStorage()
        storage2.reload()
        all_objs = storage2.all()

        self.assertIn("BaseModel.{}".format(bm1.id), all_objs.keys())
        self.assertEqual(bm1.id, all_objs["BaseModel.{}".format(bm1.id)].id)
        self.assertEqual(bm1.created_at,
                         all_objs["BaseModel.{}".format(bm1.id)].created_at)
        self.assertEqual(bm1.updated_at,
                         all_objs["BaseModel.{}".format(bm1.id)].updated_at)

        self.assertIn("BaseModel.{}".format(bm2.id), all_objs.keys())
        self.assertEqual(bm2.id, all_objs["BaseModel.{}".format(bm2.id)].id)
        self.assertEqual(bm2.created_at,
                         all_objs["BaseModel.{}".format(bm2.id)].created_at)
        self.assertEqual(bm2.updated_at,
                         all_objs["BaseModel.{}".format(bm2.id)].updated_at)


if __name__ == '__main__':
    unittest.main()
