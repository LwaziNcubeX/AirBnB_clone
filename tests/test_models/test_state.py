#!/use/bin/python3
"""
This module contains the unit tests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """
    def test_state_name(self):
        """
        Test that the name attribute of a State instance can
        be set and retrieved.
        """
        state = State()
        self.assertEqual(state.name, "")

        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_str(self):
        """
        Test the __str__ method of a State instance.
        """
        state = State()
        state.name = "California"
        state_str = str(state)
        self.assertIn("[State]", state_str)
        self.assertIn("'id': '{}'".format(state.id), state_str)
        self.assertIn("'name': '{}'".format(state.name), state_str)


if __name__ == '__main__':
    unittest.main()
