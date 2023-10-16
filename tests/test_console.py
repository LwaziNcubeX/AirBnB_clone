#!/usr/bin/python3
"""unit tests for console"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class, which provides
    a command line interface for interacting with a
    database of objects.
    """

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {model_id}")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(
                f"update BaseModel {model_id} first_name 'John'")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {model_id}")
            self.console.onecmd(f"show BaseModel {model_id}")
            self.assertTrue("** no instance found **" in f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
