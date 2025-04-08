from unittest import TestCase
import check


class Test(TestCase):

    def test_check_if_goal_attained_level_one(self):
        character_test = {"Level": 1, "Stamina": 6}
        expected = check.check_if_goal_attained(character_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_level_one_no_stamina(self):
        character_test = {"Level": 1, "Stamina": 0}
        expected = check.check_if_goal_attained(character_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_level_three(self):
        character_test = {"Level": 3, "Stamina": 1}
        expected = check.check_if_goal_attained(character_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_level_three_no_stamina(self):
        character_test = {"Level": 3, "Stamina": 0}
        expected = check.check_if_goal_attained(character_test)
        actual = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_level_five(self):
        character_test = {"Level": 5, "Stamina": 1}
        expected = check.check_if_goal_attained(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_level_five_no_stamina(self):
        character_test = {"Level": 5, "Stamina": 0}
        expected = check.check_if_goal_attained(character_test)
        actual = False
        self.assertEqual(expected, actual)