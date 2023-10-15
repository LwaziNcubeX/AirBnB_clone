#!/use/bin/python3
"""
This module contains the unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """
    def test_amenity_name(self):
        """
        Test that the name attribute of an Amenity instance
        can be set and retrieved.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_str(self):
        """
        Test the __str__ method of an Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "WiFi"
        amenity_str = str(amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("'id': '{}'".format(amenity.id), amenity_str)
        self.assertIn("'name': '{}'".format(amenity.name), amenity_str)


if __name__ == '__main__':
    unittest.main()
