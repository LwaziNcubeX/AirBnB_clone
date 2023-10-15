#!/use/bin/python3
"""
This module contains the unit tests for the User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def test_user_attributes(self):
        """
        Test that the attributes of a User instance can be set and retrieved.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        user.email = "john.doe@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_str(self):
        """
        Test the __str__ method of a User instance.
        """
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_str = str(user)
        self.assertIn("[User]", user_str)
        self.assertIn("'id': '{}'".format(user.id), user_str)
        self.assertIn("'email': '{}'".format(user.email), user_str)
        self.assertIn("'password': '{}'".format(user.password), user_str)
        self.assertIn("'first_name': '{}'".format(user.first_name), user_str)
        self.assertIn("'last_name': '{}'".format(user.last_name), user_str)


if __name__ == '__main__':
    unittest.main()
