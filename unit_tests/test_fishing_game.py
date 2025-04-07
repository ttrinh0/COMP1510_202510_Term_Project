from unittest import TestCase, mock
from unittest.mock import patch
import io
from color50 import rgb, constants

import user_action
import setup


class Test(TestCase):

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["1"])
    def test_fishing_game_win_one(self, _, __):
        character_test = {"Level": 1, "Fishing Power": 4, "Fish Caught": 0, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        expected = character_test
        actual = {"Level": 1, "Fishing Power": 4, "Fish Caught": 1, "Stamina": 6}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=["2", "2"])
    def test_fishing_game_win_two(self, _, __):
        character_test = {"Level": 2, "Fishing Power": 4, "Fish Caught": 0, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        expected = character_test
        actual = {"Level": 2, "Fishing Power": 4, "Fish Caught": 1, "Stamina": 6}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["2"])
    def test_fishing_game_lose_wrong_key(self, _, __):
        character_test = {"Level": 1, "Fishing Power": 4, "Fish Caught": 0, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        expected = character_test
        actual = {"Level": 1, "Fishing Power": 4, "Fish Caught": 0, "Stamina": 5}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["1"])
    @mock.patch('time.time', mock.MagicMock(side_effect=[1, 5]))
    def test_fishing_game_lose_too_slow(self, _, __):
        character_test = {"Level": 1, "Fishing Power": 5, "Fish Caught": 0, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        expected = character_test
        actual = {"Level": 1, "Fishing Power": 5, "Fish Caught": 0, "Stamina": 5}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fishing_game_level_one_win_print(self, mock_output, _, __):
        character_test = {"Level": 1, "Fishing Power": 4, "Fish Caught": 1, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        print_one = ("You cast your rod.\nInput the specified key within 3.0 seconds when prompted!\n...\n\n"
                     "Something hooks!\n")
        print_two = rgb(255, 255, 0) + "\tHIT!" + constants.RESET + "\nGotcha!\n"
        expected = print_one + print_two
        self.assertEqual(expected, mock_output.getvalue())

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["3", "3", "3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fishing_game_level_four_win_print(self, mock_output, _, __):
        character_test = {"Level": 3, "Fishing Power": 10, "Fish Caught": 1, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        print_one = ("You cast your rod.\nInput the specified key within 2.0 seconds when prompted!\n...\n...\n...\n\n"
                     "Something hooks!\n")
        print_two = rgb(255, 255, 0) + "\tHIT!" + constants.RESET + "\n"
        print_three = "Gotcha!\n"
        expected = print_one + print_two + print_two + print_two + print_three
        self.assertEqual(expected, mock_output.getvalue())

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fishing_game_level_one_lose_print(self, mock_output, _, __):
        character_test = {"Level": 1, "Fishing Power": 4, "Fish Caught": 2, "Stamina": 6}
        game_parameters_test = setup.create_game_parameters()
        user_action.fishing_game(character_test, game_parameters_test)
        print_one = ("You cast your rod.\nInput the specified key within 3.0 seconds when prompted!\n...\n\n"
                     "Something hooks!\n")
        print_two = "\nThe fish breaks free and gets away...\nYour stamina decreases by 1\nCurrent stamina: 5\n"
        expected = print_one + print_two
        self.assertEqual(expected, mock_output.getvalue())