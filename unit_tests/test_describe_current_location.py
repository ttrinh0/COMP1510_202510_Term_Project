from unittest import TestCase
import io
from unittest.mock import patch
from color50 import rgb, constants
import setup
import print_or_scene

class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Stamina": 5}
        print_or_scene.describe_current_location(board_test, character_test)
        expected = rgb(240, 230, 150) + "You are currently at (0, 0)." + constants.RESET + "\n"
        self.assertEqual(expected, mock_output.getvalue())
