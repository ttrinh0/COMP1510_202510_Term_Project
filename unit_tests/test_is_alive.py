from unittest import TestCase
import check


class Test(TestCase):

    def test_is_alive_five_hp(self):
        character_test = {"Stamina": 5}
        expected = check.is_alive(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_is_alive_four_hp(self):
        character_test = {"Stamina": 4}
        expected = check.is_alive(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_is_alive_three_hp(self):
        character_test = {"Stamina": 3}
        expected = check.is_alive(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_is_alive_two_hp(self):
        character_test = {"Stamina": 2}
        expected = check.is_alive(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_is_alive_one_hp(self):
        character_test = {"Stamina": 1}
        expected = check.is_alive(character_test)
        actual = True
        self.assertEqual(expected, actual)

    def test_is_alive_zero_hp(self):
        character_test = {"Stamina": 0}
        expected = check.is_alive(character_test)
        actual = False
        self.assertEqual(expected, actual)