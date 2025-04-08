from unittest import TestCase
import user_action


class Test(TestCase):

    def test_add_fish_to_collection_empty(self):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'), 2: ("???", "???"), 3: ("???", "???"),
                                              4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_test = (2, ('Guppy', 'A tiny little fella. A little, little fish.'))
        user_action.add_fish_to_collection(character_test, fish_test)
        expected = character_test
        actual = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                      3: ("???", "???"), 4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
                                      7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"), 10: ("???", "???"),
                                      11: ("???", "???")}}
        self.assertEqual(expected, actual)

    def test_add_fish_to_collection_half_full(self):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra', 'A small fish with a bright line to light up your '
                                                                'life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'), 5: ('Catfish', 'It\'s hissing at'
                                                                                                      ' you...'),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
                                              10: ("???", "???"), 11: ("???", "???")}}
        fish_test = (7, ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this glue doing here?"))
        user_action.add_fish_to_collection(character_test, fish_test)
        expected = character_test
        actual = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                      3: ('Neon Tetra', 'A small fish with a bright line to light up your life.'),
                                      4: ('Dogfish', 'Weird dog, er-- fish.'),
                                      5: ('Catfish', 'It\'s hissing at you...'),
                                      6: ('River Trout', 'How does this affect the trout population?'),
                                      7: ('Tuna',
                                          "Can't piano a tuna, but you can tuna piano! Hey, what's this glue doing "
                                          "here?"),
                                      8: ("???", "???"),
                                      9: ("???", "???"),
                                      10: ("???", "???"),
                                      11: ("???", "???")}}
        self.assertEqual(expected, actual)

    def test_add_fish_to_collection_last_fish(self):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra', 'A small fish with a bright line to light up your '
                                                                'life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'), 5: ('Catfish', 'It\'s hissing at'
                                                                                                      ' you...'),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this"
                                                          " glue doing here?"),
                                              8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's..."
                                                             " incredibly shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: ('???', '???')}}
        fish_test = (11, ('Final Fishasy', 'The legendary fish... and now it\'s in your bucket.'))
        user_action.add_fish_to_collection(character_test, fish_test)
        expected = character_test
        actual = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                      2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                      3: ('Neon Tetra', 'A small fish with a bright line to light up your life.'),
                                      4: ('Dogfish', 'Weird dog, er-- fish.'),
                                      5: ('Catfish', 'It\'s hissing at you...'),
                                      6: ('River Trout', 'How does this affect the trout population?'),
                                      7: ('Tuna',
                                          "Can't piano a tuna, but you can tuna piano! Hey, what's this glue doing "
                                          "here?"),
                                      8: ('Bigfish',
                                          "Small in size, but big in heart. It's blue, and it's... incredibly shiny"),
                                      9: ('Flying Fish', 'It practically flew into your boat!'),
                                      10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                      11: ('Final Fishasy', 'The legendary fish... and now it\'s in your bucket.')}}
        self.assertEqual(expected, actual)
