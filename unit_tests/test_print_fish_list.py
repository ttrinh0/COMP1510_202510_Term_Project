from unittest import TestCase
from unittest.mock import patch
import print_or_scene
import io
from color50 import rgb, constants


class Test(TestCase):

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_fish_list_empty_collection_false(self, mock_output, _):
        character_test = {'Fish Collection': {1: ('???', '???'),
                                              2: ('???', '???'),
                                              3: ('???', '???'),
                                              4: ('???', '???'), 5: ('???', '???'),
                                              6: ('???', '???'),
                                              7: ('???', '???'),
                                              8: ('???', '???'),
                                              9: ('???', '???'),
                                              10: ('???', '???'),
                                              11: ('???', '???')}}
        print_or_scene.print_fish_list(character_test)
        expected = """\tFish Collection
-----------------------
1: ???
2: ???
3: ???
4: ???
5: ???
6: ???
7: ???
8: ???
9: ???
10: ???
11: ???
-----------------------\n"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_fish_list_full_collection_false(self, mock_output, _):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', 'It\'s hissing at you...'),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna',
                                                  "Can't piano a tuna, but you can tuna piano! Hey, what's this glue "
                                                  "doing here?"),
                                              8: ('Bigfish',
                                                  "Small in size, but big in heart. It's blue, and it's... incredibly "
                                                  "shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: ('Final Fishasy',
                                                   'The legendary fish... and now it\'s in your bucket.')}}
        print_or_scene.print_fish_list(character_test)
        expected = """\tFish Collection
-----------------------
1: Goldfish
2: Guppy
3: Neon Tetra
4: Dogfish
5: Catfish
6: River Trout
7: Tuna
8: Bigfish
9: Flying Fish
10: Shark
11: Final Fishasy
-----------------------\n"""
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "q"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_fish_list_empty_collection_true(self, mock_output, _):
        character_test = {'Fish Collection': {1: ('???', '???'),
                                              2: ('???', '???'),
                                              3: ('???', '???'),
                                              4: ('???', '???'), 5: ('???', '???'),
                                              6: ('???', '???'),
                                              7: ('???', '???'),
                                              8: ('???', '???'),
                                              9: ('???', '???'),
                                              10: ('???', '???'),
                                              11: ('???', '???')}}
        print_or_scene.print_fish_list(character_test, True)
        print_two = rgb(255, 255, 255) + "???" + constants.RESET
        expected = """\tFish Collection
-----------------------
1: ???
2: ???
3: ???
4: ???
5: ???
6: ???
7: ???
8: ???
9: ???
10: ???
11: ???
-----------------------\n""" + print_two + ": You have not unlocked this fish yet!\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "q"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_fish_list_full_collection_true(self, mock_output, _):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', 'It\'s hissing at you...'),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna',
                                                  "Can't piano a tuna, but you can tuna piano! Hey, what's this glue "
                                                  "doing here?"),
                                              8: ('Bigfish',
                                                  "Small in size, but big in heart. It's blue, and it's... incredibly "
                                                  "shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: ('Final Fishasy',
                                                   'The legendary fish... and now it\'s in your bucket.')}}
        print_or_scene.print_fish_list(character_test, True)
        print_two = rgb(255, 255, 255) + "Goldfish" + constants.RESET
        expected = """\tFish Collection
-----------------------
1: Goldfish
2: Guppy
3: Neon Tetra
4: Dogfish
5: Catfish
6: River Trout
7: Tuna
8: Bigfish
9: Flying Fish
10: Shark
11: Final Fishasy
-----------------------\n""" + print_two + ": BUY GOLD!\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=["1", "", "q"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_fish_list_full_collection_true_view_next(self, mock_output, _):
        character_test = {'Fish Collection': {1: ('Goldfish', 'BUY GOLD!'),
                                              2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                              3: ('Neon Tetra',
                                                  'A small fish with a bright line to light up your life.'),
                                              4: ('Dogfish', 'Weird dog, er-- fish.'),
                                              5: ('Catfish', 'It\'s hissing at you...'),
                                              6: ('River Trout', 'How does this affect the trout population?'),
                                              7: ('Tuna',
                                                  "Can't piano a tuna, but you can tuna piano! Hey, what's this glue "
                                                  "doing here?"),
                                              8: ('Bigfish',
                                                  "Small in size, but big in heart. It's blue, and it's... incredibly "
                                                  "shiny"),
                                              9: ('Flying Fish', 'It practically flew into your boat!'),
                                              10: ('Shark', 'Doo doo doo, doo doo doo doo doo.'),
                                              11: ('Final Fishasy',
                                                   'The legendary fish... and now it\'s in your bucket.')}}
        print_or_scene.print_fish_list(character_test, True)
        print_two = rgb(255, 255, 255) + "Goldfish" + constants.RESET
        print_three = rgb(255, 255, 255) + "Guppy" + constants.RESET
        expected = ("""\tFish Collection
-----------------------
1: Goldfish
2: Guppy
3: Neon Tetra
4: Dogfish
5: Catfish
6: River Trout
7: Tuna
8: Bigfish
9: Flying Fish
10: Shark
11: Final Fishasy
-----------------------\n""" + print_two + ": BUY GOLD!\n" + print_three +
                    ": A tiny little fella. A little, little fish.\n")
        self.assertEqual(expected, mock_output.getvalue())
