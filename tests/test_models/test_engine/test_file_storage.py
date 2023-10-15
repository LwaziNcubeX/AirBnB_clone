#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_FileStorage_instance(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_Objects_dict(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_FilePath_str(self):
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.assertIn("BaseModel.{}".format(bm1.id), self.storage.all().keys())
        self.assertIn(bm1, self.storage.all().values())

        self.storage.new(bm2)
        self.assertIn("BaseModel.{}".format(bm2.id), self.storage.all().keys())
        self.assertIn(bm2, self.storage.all().values())

    def test_save(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as f:
            file_contents = f.read()

        self.assertIn("BaseModel.{}".format(bm1.id), file_contents)
        self.assertIn('updated_at', file_contents)
        self.assertIn("BaseModel.{}".format(bm2.id), file_contents)
        self.assertIn('created_at', file_contents)

    def test_reload(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        self.storage.reload()

        objs = self.storage.all().values()


if __name__ == '__main__':
    unittest.main()
