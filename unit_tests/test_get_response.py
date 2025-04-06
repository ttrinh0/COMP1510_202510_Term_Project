from unittest import TestCase
from unittest.mock import patch
import io
from color50 import rgb, constants

import user_action


class Test(TestCase):

    @patch('builtins.input', side_effect="1")
    def test_get_response_single_option(self, _):
        message_test = "Please input 1: "
        options_test = 1
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="3")
    def test_get_response_three_option(self, _):
        message_test = "Please input 1, 2, or 3: "
        options_test = 3
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="9")
    def test_get_response_ten_option(self, _):
        message_test = "Please input a number from 1 to 10: "
        options_test = 10
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "9"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="1")
    def test_get_response_ten_option_user_one(self, _):
        message_test = "Please input a number from 1 to 10: "
        options_test = 10
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="q")
    def test_get_response_quit(self, _):
        message_test = "Please input a number from 1 to 10 or q to quit: "
        options_test = 10
        expected = user_action.get_response(message_test, options_test, True)
        actual = "q"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["7", "5"])
    def test_get_response_user_input_invalid_integer(self, _):
        message_test = "Please input a number from 1 to 5: "
        options_test = 5
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["g", "5"])
    def test_get_response_user_input_invalid_string(self, _):
        message_test = "Please input a number from 1 to 5: "
        options_test = 5
        expected = user_action.get_response(message_test, options_test, option_quit=False)
        actual = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["g", "5"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_response_user_input_invalid_print(self, mock_output, _):
        message_test = "Please input a number from 1 to 5: "
        options_test = 5
        user_action.get_response(message_test, options_test, option_quit=False)
        expected = rgb(255, 175, 175) + "Please enter a valid option!" + constants.RESET + "\n"
        self.assertEqual(expected, mock_output.getvalue())