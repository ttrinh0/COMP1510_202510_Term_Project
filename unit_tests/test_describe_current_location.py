from unittest import TestCase
import io
from unittest.mock import patch
from color50 import rgb, constants
import setup
import print_or_scene


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_start_empty(self, mock_output):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Stamina": 5}
        print_or_scene.describe_current_location(board_test, character_test)
        expected = rgb(240, 230, 150) + "You are currently at (0, 0)." + constants.RESET + "\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_last_empty(self, mock_output):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Stamina": 5}
        print_or_scene.describe_current_location(board_test, character_test)
        expected = rgb(240, 230, 150) + "You are currently at (2, 2)." + constants.RESET + "\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_fisher(self, mock_output):
        board_test = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''),
                      (0, 4): ('', ''), (1, 0): ('', ''), (1, 1): ('', ''), (1, 2): ('', ''),
                      (1, 3): ('', ''), (1, 4): ('', ''), (2, 0): ('', ''), (2, 1): ('', ''),
                      (2, 2): ('', ''), (2, 3): ('Fisher', 'Name'), (2, 4): ('', ''), (3, 0): ('', ''),
                      (3, 1): ('', ''), (3, 2): ('', ''), (3, 3): ('', ''), (3, 4): ('', ''),
                      (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('', ''),
                      (4, 4): ('', '')}
        character_test = {"X-coordinate": 2, "Y-coordinate": 3, "Stamina": 5}
        print_or_scene.describe_current_location(board_test, character_test)
        expected = (rgb(240, 230, 150) + "You are currently at (2, 3). There's a fisher nearby."
                    + constants.RESET + "\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_coin(self, mock_output):
        board_test = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''),
                      (0, 4): ('', ''), (1, 0): ('', ''), (1, 1): ('', ''), (1, 2): ('', ''),
                      (1, 3): ('', ''), (1, 4): ('', ''), (2, 0): ('', ''), (2, 1): ('', ''),
                      (2, 2): ('', ''), (2, 3): ('Coin', 'Name'), (2, 4): ('', ''), (3, 0): ('', ''),
                      (3, 1): ('', ''), (3, 2): ('', ''), (3, 3): ('', ''), (3, 4): ('', ''),
                      (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('', ''),
                      (4, 4): ('', '')}
        character_test = {"X-coordinate": 2, "Y-coordinate": 3, "Stamina": 5}
        print_or_scene.describe_current_location(board_test, character_test)
        expected = (rgb(240, 230, 150) + "You are currently at (2, 3). There's something on that rock."
                    + constants.RESET + "\n")
        self.assertEqual(expected, mock_output.getvalue())