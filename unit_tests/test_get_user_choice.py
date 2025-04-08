from unittest import TestCase
from unittest.mock import patch
import user_action


class Test(TestCase):

    @patch('builtins.input', side_effect="w")
    def test_get_user_choice_w_lower(self, _):
        expected = user_action.get_user_choice()
        actual = "North"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="W")
    def test_get_user_choice_w_upper(self, _):
        expected = user_action.get_user_choice()
        actual = "North"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="a")
    def test_get_user_choice_a_lower(self, _):
        expected = user_action.get_user_choice()
        actual = "West"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="A")
    def test_get_user_choice_a_upper(self, _):
        expected = user_action.get_user_choice()
        actual = "West"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="d")
    def test_get_user_choice_d_lower(self, _):
        expected = user_action.get_user_choice()
        actual = "East"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="D")
    def test_get_user_choice_d_upper(self, _):
        expected = user_action.get_user_choice()
        actual = "East"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="s")
    def test_get_user_choice_s_lower(self, _):
        expected = user_action.get_user_choice()
        actual = "South"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="S")
    def test_get_user_choice_s_upper(self, _):
        expected = user_action.get_user_choice()
        actual = "South"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="1")
    def test_get_user_choice_fish(self, _):
        expected = user_action.get_user_choice()
        actual = "Fish"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="2")
    def test_get_user_choice_interact(self, _):
        expected = user_action.get_user_choice()
        actual = "Interact"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="3")
    def test_get_user_choice_profile(self, _):
        expected = user_action.get_user_choice()
        actual = "Profile"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="4")
    def test_get_user_choice_collection(self, _):
        expected = user_action.get_user_choice()
        actual = "Collection"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="s")
    @patch('builtins.input', side_effect="F")
    def test_get_user_choice_one_incorrect(self, _, __):
        expected = user_action.get_user_choice()
        actual = "South"
        self.assertEqual(expected, actual)
