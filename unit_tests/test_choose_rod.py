from unittest import TestCase
from unittest.mock import patch
import io
from color50 import rgb, constants

import setup


class Test(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_choose_rod_stamina(self, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        setup.choose_rod(character_test)
        expected = character_test
        actual = {"Stamina": 6, "Max Stamina": 6, "Fishing Power": 4}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1"])
    def test_choose_rod_stamina_return(self, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        expected = setup.choose_rod(character_test)
        actual = "Stamina Rod"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_choose_rod_power(self, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        setup.choose_rod(character_test)
        expected = character_test
        actual = {"Stamina": 4, "Max Stamina": 4, "Fishing Power": 6}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_choose_rod_power_return(self, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        expected = setup.choose_rod(character_test)
        actual = "Power Rod"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["g", "1"])
    def test_choose_rod_one_invalid(self, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        setup.choose_rod(character_test)
        expected = character_test
        actual = {"Stamina": 6, "Max Stamina": 6, "Fishing Power": 4}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["g", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_rod_one_invalid_print(self, mock_output, _):
        character_test = {"Stamina": 1, "Max Stamina": 1, "Fishing Power": 1}
        setup.choose_rod(character_test)
        print_one = rgb(0, 255, 255) + "Which rod did you pick?: \n"
        print_two = rgb(240, 230, 150) + '"Sorry, I didn\'t quite catch that!"\n'
        print_three = rgb(255, 175, 175) + '(Please enter 1 or 2 to select your fishing rod)' + constants.RESET + '\n'
        expected = print_one + print_two + print_three
        self.assertEqual(expected, mock_output.getvalue())