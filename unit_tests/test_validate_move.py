from unittest import TestCase
import check
import setup


class Test(TestCase):

    def test_validate_move_valid_south(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "South"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_south(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
        direction_test = "South"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_validate_move_valid_north(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        direction_test = "North"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_north(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "North"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_validate_move_valid_east(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "East"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_east(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "East"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_validate_move_valid_west(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "West"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_west(self):
        board_test = setup.make_board(3, 3)
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction_test = "West"
        expected = check.validate_move(board_test, character_test, direction_test)
        actual = False
        self.assertEqual(expected, actual)