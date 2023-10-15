#!/usr/bin/python3
"""
This module contains the unit tests for the Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def test_place_attributes(self):
        """
        Test that the attributes of a Place instance can be set and retrieved.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        place.city_id = "SF"
        place.user_id = "1234"
        place.name = "Cozy Apartment"
        place.description = "A very nice place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool"]

        self.assertEqual(place.city_id, "SF")
        self.assertEqual(place.user_id, "1234")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A very nice place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 150)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "pool"])

    def test_place_str(self):
        """
        Test the __str__ method of a Place instance.
        """
        place = Place()
        place.city_id = "SF"
        place.user_id = "1234"
        place.name = "Cozy Apartment"
        place.description = "A very nice place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool"]

        place_str = str(place)
        self.assertIn("[Place]", place_str)
        self.assertIn("'id': '{}'".format(place.id), place_str)
        self.assertIn("'city_id': '{}'".format(place.city_id), place_str)
        self.assertIn("'user_id': '{}'".format(place.user_id), place_str)
        self.assertIn("'name': '{}'".format(place.name), place_str)
        self.assertIn("'description': '{}'".format(place.description),
                      place_str)
        self.assertIn("'number_rooms': {}".format(place.number_rooms),
                      place_str)
        self.assertIn("'number_bathrooms': {}".format(place.number_bathrooms),
                      place_str)
        self.assertIn("'max_guest': {}".format(place.max_guest), place_str)
        self.assertIn("'price_by_night': {}".format(place.price_by_night),
                      place_str)
        self.assertIn("'latitude': {}".format(place.latitude), place_str)
        self.assertIn("'longitude': {}".format(place.longitude), place_str)


if __name__ == '__main__':
    unittest.main()
