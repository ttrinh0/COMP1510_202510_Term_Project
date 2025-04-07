from unittest import TestCase
from unittest.mock import patch

import setup


class Test(TestCase):

    @patch('builtins.input', side_effect=[""])
    def test_get_name_leave_blank(self, _):
        character_test = {"Name": ""}
        setup.get_name(character_test)
        expected = character_test
        actual = {"Name": ""}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["John"])
    def test_get_name_string(self, _):
        character_test = {"Name": ""}
        setup.get_name(character_test)
        expected = character_test
        actual = {"Name": "John"}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["123"])
    def test_get_name_input_number(self, _):
        character_test = {"Name": ""}
        setup.get_name(character_test)
        expected = character_test
        actual = {"Name": "123"}
        self.assertEqual(expected, actual)