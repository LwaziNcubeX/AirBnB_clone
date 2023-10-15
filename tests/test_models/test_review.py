#!/use/bin/python3
"""
This module contains the unit tests for the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class.
    """
    def test_review_attributes(self):
        """
        Test that the attributes of a Review instance can be set and retrieved.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        review.place_id = "1234"
        review.user_id = "5678"
        review.text = "A great place to stay!"

        self.assertEqual(review.place_id, "1234")
        self.assertEqual(review.user_id, "5678")
        self.assertEqual(review.text, "A great place to stay!")

    def test_review_str(self):
        """
        Test the __str__ method of a Review instance.
        """
        review = Review()
        review.place_id = "1234"
        review.user_id = "5678"
        review.text = "A great place to stay!"

        review_str = str(review)
        self.assertIn("[Review]", review_str)
        self.assertIn("'id': '{}'".format(review.id), review_str)
        self.assertIn("'place_id': '{}'".format(review.place_id), review_str)
        self.assertIn("'user_id': '{}'".format(review.user_id), review_str)
        self.assertIn("'text': '{}'".format(review.text), review_str)


if __name__ == '__main__':
    unittest.main()
