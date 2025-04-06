from unittest import TestCase
import io
from unittest.mock import patch

import check


class Test(TestCase):

    @patch('random.randint', return_value=2)
    def test_check_for_fish_two_encounter(self, _):
        character_test = {"Fish Limit": 0}
        expected = check.check_for_fish(character_test)
        actual = True
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_check_for_fish_three_encounter(self, _):
        character_test = {"Fish Limit": 0}
        expected = check.check_for_fish(character_test)
        actual = True
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_fish_no_encounter(self, mock_output, _):
        character_test = {"Fish Limit": 0}
        check.check_for_fish(character_test)
        expected = "You cast your rod.\n...\n...\nNothing's biting.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_fish_fish_limit_three(self, mock_output):
        character_test = {"Fish Limit": 3}
        check.check_for_fish(character_test)
        expected = "You cast your rod.\n...\n...\nNothing's biting. It might be time to move to another spot.\n"
        self.assertEqual(expected, mock_output.getvalue())