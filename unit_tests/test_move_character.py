from unittest import TestCase
import user_action


class Test(TestCase):

    def test_move_character_south(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        direction_test = "South"
        user_action.move_character(character_test, direction_test)
        expected = character_test
        actual = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Fish Limit": 0}
        self.assertEqual(expected, actual)

    def test_move_character_north(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Fish Limit": 0}
        direction_test = "North"
        user_action.move_character(character_test, direction_test)
        expected = character_test
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character_test = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        direction_test = "West"
        user_action.move_character(character_test, direction_test)
        expected = character_test
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character_test = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        direction_test = "East"
        user_action.move_character(character_test, direction_test)
        expected = character_test
        actual = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        self.assertEqual(expected, actual)

    def test_move_character_east_two_fish_limit(self):
        character_test = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 2}
        direction_test = "East"
        user_action.move_character(character_test, direction_test)
        expected = character_test
        actual = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
        self.assertEqual(expected, actual)