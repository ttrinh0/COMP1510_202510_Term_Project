from unittest import TestCase
import setup


class Test(TestCase):

    def test_add_on_board_level_one(self):
        game_parameters_test = setup.create_game_parameters()
        coordinates_test = setup.make_board(5, 5)
        character_test = {"Level": 1}
        expected = setup.add_on_board(game_parameters_test, coordinates_test, character_test)
        actual = {(0, 0): ('', ''), (0, 1): ('Fisher', 'Sally'), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', ''),
                  (1, 0): ('', ''), (1, 1): ('', ''), (1, 2): ('', ''), (1, 3): ('', ''), (1, 4): ('', ''),
                  (2, 0): ('', ''), (2, 1): ('', ''), (2, 2): ('', ''), (2, 3): ('', ''), (2, 4): ('Fisher', 'Rob'),
                  (3, 0): ('', ''), (3, 1): ('', ''), (3, 2): ('', ''), (3, 3): ('', ''), (3, 4): ('', ''),
                  (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('Fisher', 'Charles'), (4, 4): ('', '')}
        self.assertEqual(expected, actual)

    def test_add_on_board_level_two(self):
        game_parameters_test = setup.create_game_parameters()
        coordinates_test = setup.make_board(5, 5)
        character_test = {"Level": 2}
        expected = setup.add_on_board(game_parameters_test, coordinates_test, character_test)
        actual = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', ''),
                  (1, 0): ('', ''), (1, 1): ('Fisher', 'Cornet'), (1, 2): ('', ''), (1, 3): ('', ''), (1, 4): ('', ''),
                  (2, 0): ('', ''), (2, 1): ('', ''), (2, 2): ('', ''), (2, 3): ('', ''), (2, 4): ('', ''),
                  (3, 0): ('', ''), (3, 1): ('', ''), (3, 2): ('Fisher', 'Sandy'), (3, 3): ('', ''), (3, 4): ('', ''),
                  (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('', ''), (4, 4): ('Fisher', 'Gilly')}
        self.assertEqual(expected, actual)

    def test_add_on_board_level_three(self):
        game_parameters_test = setup.create_game_parameters()
        coordinates_test = setup.make_board(5, 5)
        character_test = {"Level": 3}
        expected = setup.add_on_board(game_parameters_test, coordinates_test, character_test)
        actual = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', ''),
                  (1, 0): ('', ''), (1, 1): ('', ''), (1, 2): ('', ''), (1, 3): ('', ''), (1, 4): ('', ''),
                  (2, 0): ('', ''), (2, 1): ('', ''), (2, 2): ('', ''), (2, 3): ('', ''), (2, 4): ('', ''),
                  (3, 0): ('Fisher', 'Emile'), (3, 1): ('', ''), (3, 2): ('', ''), (3, 3): ('', ''), (3, 4): ('', ''),
                  (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('', ''), (4, 4): ('Fisher', 'Aqua')}
        self.assertEqual(expected, actual)

    def test_add_on_board_level_four(self):
        game_parameters_test = setup.create_game_parameters()
        coordinates_test = setup.make_board(5, 5)
        character_test = {"Level": 4}
        expected = setup.add_on_board(game_parameters_test, coordinates_test, character_test)
        actual = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', ''),
                  (1, 0): ('', ''), (1, 1): ('', ''), (1, 2): ('', ''), (1, 3): ('', ''), (1, 4): ('', ''),
                  (2, 0): ('', ''), (2, 1): ('', ''), (2, 2): ('Coin', 'Coin'), (2, 3): ('', ''), (2, 4): ('', ''),
                  (3, 0): ('', ''), (3, 1): ('', ''), (3, 2): ('', ''), (3, 3): ('', ''), (3, 4): ('', ''),
                  (4, 0): ('', ''), (4, 1): ('', ''), (4, 2): ('', ''), (4, 3): ('', ''), (4, 4): ('', '')}
        self.assertEqual(expected, actual)
