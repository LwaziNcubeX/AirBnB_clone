#!/use/bin/python3
"""
This module contains the unit tests for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """
    def test_city_attributes(self):
        """
        Test that the attributes of a City instance can be set and retrieved.
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

        city.name = "San Francisco"
        city.state_id = "CA"
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")

    def test_city_str(self):
        """
        Test the __str__ method of a City instance.
        """
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        city_str = str(city)
        self.assertIn("[City]", city_str)
        self.assertIn("'id': '{}'".format(city.id), city_str)
        self.assertIn("'state_id': '{}'".format(city.state_id), city_str)
        self.assertIn("'name': '{}'".format(city.name), city_str)


if __name__ == '__main__':
    unittest.main()
