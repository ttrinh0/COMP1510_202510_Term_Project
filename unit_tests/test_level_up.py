from unittest import TestCase
from unittest.mock import patch

import check
import setup


class Test(TestCase):

    @patch('builtins.input', side_effect="")
    def test_level_up_level_one_no_level_up(self, _):
        character_test = {"Level": 1, "Stamina": 5, "Max Stamina": 5, "Fishing Power": 5, "Title": "Beginner Fisher",
                          "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"),
                                              4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        expected = check.level_up(character_test, fish_collection)
        actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="")
    def test_level_up_level_one_no_level_up_character(self, _):
        character_test = {"Level": 1, "Stamina": 5, "Max Stamina": 5, "Fishing Power": 5, "Title": "Beginner Fisher",
                          "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"),
                                              4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        check.level_up(character_test, fish_collection)
        expected = character_test
        actual = {"Level": 1, "Stamina": 5, "Max Stamina": 5, "Fishing Power": 5, "Title": "Beginner Fisher",
                  "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"),
                                      4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                      7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                      10: ("???", "???"), 11: ("???", "???")}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_one_level_up(self, _):
        character_test = {"Level": 1, "Stamina": 5, "Max Stamina": 5, "Fishing Power": 5,
                          "Title": "Beginner Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        expected = check.level_up(character_test, fish_collection)
        actual = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_one_level_up_character(self, _):
        character_test = {"Level": 1, "Stamina": 5, "Max Stamina": 5, "Fishing Power": 5,
                          "Title": "Beginner Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        check.level_up(character_test, fish_collection)
        expected = character_test
        actual = {'Level': 2, 'Stamina': 6, 'Max Stamina': 6, 'Fishing Power': 6,
                  'Title': 'Adept Fisher',
                  'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy',
                                          'A tiny little fella. A little, little fish.'),
                                      3: ('Neon Tetra',
                                          'A small fish with a bright line to light up your life.'),
                                      4: ('???', '???'), 5: ('???', '???'), 6: ('???', '???'),
                                      7: ('???', '???'), 8: ('???', '???'), 9: ('???', '???'),
                                      10: ('???', '???'), 11: ('???', '???')}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_three_level_up(self, _):
        character_test = {"Level": 3, "Stamina": 7, "Max Stamina": 7, "Fishing Power": 9,
                          "Title": "Expert Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', "It's hissing at you..."),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                          " glue doing here?"),
                                              8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                             " incredibly shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        expected = check.level_up(character_test, fish_collection)
        actual = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_three_level_up_character(self, _):
        character_test = {"Level": 3, "Stamina": 7, "Max Stamina": 7, "Fishing Power": 9,
                          "Title": "Expert Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', "It's hissing at you..."),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                          " glue doing here?"),
                                              8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                             " incredibly shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'), 11: ("???", "???")}}
        fish_collection = setup.make_fish_collection()
        check.level_up(character_test, fish_collection)
        expected = character_test
        actual = {"Level": 4, "Stamina": 8, "Max Stamina": 8, "Fishing Power": 10,
                  "Title": "Legendary Fisher",
                  "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                      3: ('Neon Tetra',
                                          'A small fish with a bright line to light up your life.'),
                                      4: ('Dogfish', 'Weird dog, er-- fish.'),
                                      5: ('Catfish', "It's hissing at you..."),
                                      6: ('River Trout', 'How does this affect the trout population?'),
                                      7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                  " glue doing here?"),
                                      8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                     " incredibly shiny"),
                                      9: ('Flying Fish', 'It practically flew into your boat!'),
                                      10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'), 11: ("???", "???")}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_four_level_up(self, _):
        character_test = {"Level": 4, "Stamina": 7, "Max Stamina": 7, "Fishing Power": 9,
                          "Title": "Legendary Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', "It's hissing at you..."),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                          " glue doing here?"),
                                              8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                             " incredibly shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: (
                                                  'Final Fishasy',
                                                  "The legendary fish... and now it's in your bucket.")}}
        fish_collection = setup.make_fish_collection()
        expected = check.level_up(character_test, fish_collection)
        actual = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["", ""])
    def test_level_up_level_four_level_up_character(self, _):
        character_test = {"Level": 4, "Stamina": 8, "Max Stamina": 8, "Fishing Power": 10,
                          "Title": "Legendary Fisher",
                          "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', "It's hissing at you..."),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                          " glue doing here?"),
                                              8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                             " incredibly shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: (
                                                  'Final Fishasy',
                                                  "The legendary fish... and now it's in your bucket.")}}
        fish_collection = setup.make_fish_collection()
        check.level_up(character_test, fish_collection)
        expected = character_test
        actual = {"Level": 5, "Stamina": 9, "Max Stamina": 9, "Fishing Power": 11,
                  "Title": "Legendary Fisher",
                  "Fish Collection": {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                      3: ('Neon Tetra',
                                          'A small fish with a bright line to light up your life.'),
                                      4: ('Dogfish', 'Weird dog, er-- fish.'),
                                      5: ('Catfish', "It's hissing at you..."),
                                      6: ('River Trout', 'How does this affect the trout population?'),
                                      7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                  " glue doing here?"),
                                      8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                     " incredibly shiny"),
                                      9: ('Flying Fish', 'It practically flew into your boat!'),
                                      10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                      11: (
                                          'Final Fishasy', "The legendary fish... and now it's in your bucket.")}}
        self.assertEqual(expected, actual)
