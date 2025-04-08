from unittest import TestCase
from unittest.mock import patch
import io
from color50 import rgb, constants
import print_or_scene


class Test(TestCase):

    @patch('builtins.input', side_effect=[""])
    @patch('random.choice', return_value="The breeze feels nice against your face.")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_interact_regular_square(self, mock_output, _, __):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Max Stamina": 5, "Stamina": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        expected = "The breeze feels nice against your face.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_interact_fisher_square_first_talk(self, mock_output, _):
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1, "Max Stamina": 5, "Stamina": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        print_one = rgb(240, 230, 150) + ('"An unfamiliar face! How exciting. I\'m Sally. I love '
                                          'fishing, it\'s relaxing.\nI really hope you enjoy your time here at '
                                          'Initium Pond!"') + constants.RESET + "\n"
        print_two = rgb(0, 255, 0) + "[Max Stamina +1!]\n" + constants.RESET + "\n"
        expected = ("You look towards the nearby fisher.\n\nThe fisher waves.\n" + print_one +
                    "The nice conversation left you in a good mood.\n\n") + print_two
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_interact_fisher_square_talked(self, mock_output, _):
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1,
                          'NPC Talk': {'Sally': True, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        print_one = rgb(240, 230, 150) + '"Enjoy your time here, fisher!"\n' + constants.RESET + "\n"
        expected = "You look towards the nearby fisher.\n\n" + print_one
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    def test_print_interact_fisher_square_first_talk_character_stats(self, _):
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1, "Max Stamina": 5, "Stamina": 5,
                          'NPC Talk': {'Sally': False,
                                       'Charles': False, 'Rob': False,
                                       'Cornet': False,
                                       'Gilly': False, 'Sandy': False,
                                       'Emile': False, 'Aqua': False,
                                       'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        actual = character_test
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1, "Max Stamina": 6, "Stamina": 6,
                    'NPC Talk': {'Sally': True,
                                 'Charles': False, 'Rob': False,
                                 'Cornet': False,
                                 'Gilly': False, 'Sandy': False,
                                 'Emile': False, 'Aqua': False,
                                 'Coin': False}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_print_interact_fisher_square_talked_character_stats(self, _):
        character_test = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1, "Max Stamina": 5, "Stamina": 5,
                          'NPC Talk': {'Sally': True,
                                       'Charles': False, 'Rob': False,
                                       'Cornet': False,
                                       'Gilly': False, 'Sandy': False,
                                       'Emile': False, 'Aqua': False,
                                       'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        actual = character_test
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Level": 1, "Max Stamina": 5, "Stamina": 5,
                    'NPC Talk': {'Sally': True,
                                 'Charles': False, 'Rob': False,
                                 'Cornet': False,
                                 'Gilly': False, 'Sandy': False,
                                 'Emile': False, 'Aqua': False,
                                 'Coin': False}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_interact_coin_square_first_interact(self, mock_output, _):
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 5,
                          "Fishing Power": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        print_one = rgb(0, 255, 0) + "[Stamina +1!]\n[Fishing Power +1!]\n" + constants.RESET + "\n"
        expected = ("You see a shiny coin on a rock. It's too far to reach, but you admire it from afar.\n"
                    "It must be a sign of good luck. You'll need it to catch the Final Fishasy.\n\n") + print_one
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_interact_coin_square_interacted(self, mock_output, _):
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 5,
                          "Fishing Power": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': True}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        expected = "The coin shines.\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[""])
    def test_print_interact_coin_square_first_interact_character(self, _):
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 4,
                          "Fishing Power": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        expected = character_test
        actual = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 5,
                  "Fishing Power": 6,
                  'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                               'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': True}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_print_interact_coin_square_first_interact_character_full_stamina(self, _):
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 5,
                          "Fishing Power": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        expected = character_test
        actual = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 5,
                  "Fishing Power": 6,
                  'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                               'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': True}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_print_interact_coin_square_interacted_character(self, _):
        character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 4,
                          "Fishing Power": 5,
                          'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                                       'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': True}}
        game_parameters_test = {"Level Map": {
            "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                      (2, 4): ("Fisher", "Rob")},
            "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                      (3, 2): ("Fisher", "Sandy")},
            "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
            "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
        print_or_scene.print_interact(character_test, game_parameters_test)
        expected = character_test
        actual = {"X-coordinate": 2, "Y-coordinate": 2, "Level": 4, "Max Stamina": 5, "Stamina": 4,
                  "Fishing Power": 5,
                  'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
                               'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': True}}
        self.assertEqual(expected, actual)
