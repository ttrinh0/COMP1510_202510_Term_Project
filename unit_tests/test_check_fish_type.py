from unittest import TestCase
from unittest.mock import patch
import check
import setup


class Test(TestCase):

    @patch('random.choice', return_value=(1, ('Goldfish', 'BUY GOLD!')))
    def test_check_fish_type_level_one(self, _):
        character_test = {"Level": 1}
        fish_collection = setup.make_fish_collection()
        expected = check.check_fish_type(character_test, fish_collection)
        actual = (1, ('Goldfish', 'BUY GOLD!'))
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=(4, ('Dogfish', 'Weird dog, er-- fish.')))
    def test_check_fish_type_level_two(self, _):
        character_test = {"Level": 2}
        fish_collection = setup.make_fish_collection()
        expected = check.check_fish_type(character_test, fish_collection)
        actual = (4, ('Dogfish', 'Weird dog, er-- fish.'))
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=(10, ('Shark', 'Doo doo doo, doo doo doo doo doo.')))
    def test_check_fish_type_level_three(self, _):
        character_test = {"Level": 3}
        fish_collection = setup.make_fish_collection()
        expected = check.check_fish_type(character_test, fish_collection)
        actual = (10, ('Shark', 'Doo doo doo, doo doo doo doo doo.'))
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=(11, ('Final Fishasy', 'The legendary fish... and now it\'s in your bucket.')))
    def test_check_fish_type_level_four(self, _):
        character_test = {"Level": 4}
        fish_collection = setup.make_fish_collection()
        expected = check.check_fish_type(character_test, fish_collection)
        actual = (11, ('Final Fishasy', 'The legendary fish... and now it\'s in your bucket.'))
        self.assertEqual(expected, actual)