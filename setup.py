"""
Module of functions that set up the game and initial character stats.
"""
from color50 import rgb, constants


def create_game_parameters() -> dict:
    """
    Create a dictionary containing the game's parameters.

    :postcondition: creates a dictionary containing the game's parameters
    :return game_parameters: a dictionary containing the game's parameters

    >>> game_parameters_test = create_game_parameters()
    >>> game_parameters_test == {'Input Time': {1: 3.0, 2: 2.5, 3: 2.0, 4: 1.5},
    ... 'Fish Reel': {1: 9, 2: 12, 3: 15, 4: 22}, 'Level Map': {'Event Coordinates One': {(0, 1): ('Fisher', 'Sally'),
    ... (4, 3): ('Fisher', 'Charles'), (2, 4): ('Fisher', 'Rob')}, 'Event Coordinates Two':
    ... {(1, 1): ('Fisher', 'Cornet'), (4, 4): ('Fisher', 'Gilly'), (3, 2): ('Fisher', 'Sandy')},
    ... 'Event Coordinates Three': {(3, 0): ('Fisher', 'Emile'), (4, 4): ('Fisher', 'Aqua')},
    ... 'Event Coordinates Final': {(2, 2): ('Coin', 'Coin')}}}
    True
    """
    game_parameters = {"Input Time": {1: 3.0, 2: 2.5, 3: 2.0, 4: 1.5}, "Fish Reel": {1: 9, 2: 12, 3: 15, 4: 22},
                       "Level Map": {
                           "Event Coordinates One": {(0, 1): ("Fisher", "Sally"), (4, 3): ("Fisher", "Charles"),
                                                     (2, 4): ("Fisher", "Rob")},
                           "Event Coordinates Two": {(1, 1): ("Fisher", "Cornet"), (4, 4): ("Fisher", "Gilly"),
                                                     (3, 2): ("Fisher", "Sandy")},
                           "Event Coordinates Three": {(3, 0): ("Fisher", "Emile"), (4, 4): ("Fisher", "Aqua")},
                           "Event Coordinates Final": {(2, 2): ("Coin", "Coin")}}}
    return game_parameters


def make_board(rows: int, columns: int) -> dict:
    """
    Return a dictionary that contains the coordinates and names of each spot on the game board.

    This function will create a game board with dimensions "rows" by "columns".

    :param rows: a positive integer greater than zero
    :param columns: a positive integer greater than zero
    :precondition: both rows and columns must be a positive integer
    :precondition: both rows and columns must be greater than zero
    :postcondition: a dictionary with keys that are tuples containing the coordinates of the board
    :postcondition: a dictionary with values containing a string representing the name of a game location
    :return coordinates: a dictionary containing key-value pairs that represent the coordinate and name of the game
                        location

    >>> make_board(1, 1)
    {(0, 0): ('', '')}
    >>> make_board(1, 5)
    {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', '')}
    """
    coordinates = {}
    for number in range(rows):
        for element in range(columns):
            coordinates[(number, element)] = ("", "")
    return coordinates


def add_on_board(game_parameters: dict, coordinates: dict, character: dict) -> dict:
    """
    Place NPCs and other visible objects onto the board depending on the player's level.

    :param game_parameters: a dictionary containing the game parameters
    :param coordinates: a dictionary containing the coordinates of the gameboard
    :param character: a dictionary containing the player's information
    :precondition: game_parameter is a dictionary with the key "Level Map" that contains a dictionary of dictionaries
                    of the coordinates of each level map NPC
    :precondition: coordinates is a dictionary containing the coordinates of the gameboard
    :precondition: character is a dictionary that contains the player's level
    :return coordinates: a dictionary containing the coordinates of the gameboard with values of tuples of the
                        NPC/object type and the name where there are NPCs or objects

    >>> game_parameters_test = {"Level Map": {"Event Coordinates One": {(0, 1): ("Fisher", "Sally")}}}
    >>> coordinates_test = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', '')}
    >>> character_test = {"Level": 1}
    >>> add_on_board(game_parameters_test, coordinates_test, character_test)
    {(0, 0): ('', ''), (0, 1): ('Fisher', 'Sally'), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', '')}
    >>> game_parameters_test = {"Level Map": {"Event Coordinates One": {(0, 1): ("Fisher", "Sally")},
    ... "Event Coordinates Two": {(0, 2): ("Fisher", "Cornet"), (0, 4): ("Fisher", "Gilly")}}}
    >>> coordinates_test = {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('', ''), (0, 3): ('', ''), (0, 4): ('', '')}
    >>> character_test = {"Level": 2}
    >>> add_on_board(game_parameters_test, coordinates_test, character_test)
    {(0, 0): ('', ''), (0, 1): ('', ''), (0, 2): ('Fisher', 'Cornet'), (0, 3): ('', ''), (0, 4): ('Fisher', 'Gilly')}
    """
    level = character["Level"]

    if level == 1:
        for coordinate in game_parameters["Level Map"]["Event Coordinates One"]:
            coordinates[coordinate] = game_parameters["Level Map"]["Event Coordinates One"][coordinate]

    elif level == 2:  # customization for level 2 map
        for coordinate in game_parameters["Level Map"]["Event Coordinates Two"]:
            coordinates[coordinate] = game_parameters["Level Map"]["Event Coordinates Two"][coordinate]

    elif level == 3:  # customization for level 3 map
        for coordinate in game_parameters["Level Map"]["Event Coordinates Three"]:
            coordinates[coordinate] = game_parameters["Level Map"]["Event Coordinates Three"][coordinate]

    elif level == 4:  # customization for boss map
        for coordinate in game_parameters["Level Map"]["Event Coordinates Final"]:
            coordinates[coordinate] = game_parameters["Level Map"]["Event Coordinates Final"][coordinate]

    return coordinates


def make_character() -> dict:  # REDO DIALOGUE
    """
    Return a dictionary containing a character's information.

    :postcondition: return a dictionary with keys: "Name", "Stamina", "Max Stamina", "Fishing Power", "X-coordinate",
                                                    "Y-coordinate", "Title", "Fish Caught", "Fish Limit",
                                                    "Fish Collection", and "NPC Talk"
    :return: a dictionary containing character information

    >>> character_test = make_character()
    >>> character_test == {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Title': 'Beginner Fisher', 'Name': '',
    ... 'Stamina': 1, 'Max Stamina': 1, 'Fishing Power': 1, 'Fish Caught': 0, 'Fish Limit': 0, 'Fish Collection':
    ... {1: ('???', '???'), 2: ('???', '???'), 3: ('???', '???'), 4: ('???', '???'), 5: ('???', '???'),
    ... 6: ('???', '???'), 7: ('???', '???'), 8: ('???', '???'), 9: ('???', '???'), 10: ('???', '???'),
    ... 11: ('???', '???')}, 'NPC Talk': {'Sally': False, 'Charles': False, 'Rob': False, 'Cornet': False,
    ... 'Gilly': False, 'Sandy': False, 'Emile': False, 'Aqua': False, 'Coin': False}}
    True
    """
    character_profile = {"X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Title": "Beginner Fisher", "Name": "",
                         "Stamina": 1, "Max Stamina": 1, "Fishing Power": 1, "Fish Caught": 0, "Fish Limit": 0,
                         "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"), 4: ("???", "???"),
                                             5: ("???", "???"), 6: ("???", "???"), 7: ("???", "???"), 8: ("???", "???"),
                                             9: ("???", "???"), 10: ("???", "???"), 11: ("???", "???")},
                         "NPC Talk": {"Sally": False, "Charles": False, "Rob": False, "Cornet": False, "Gilly": False,
                                      "Sandy": False, "Emile": False, "Aqua": False, "Coin": False}}
    return character_profile


def get_name(character: dict):
    """
    Ask the player for their name.

    :param character: a dictionary with the character information
    :precondition: the player inputs a name (or any string/value)
    :precondition: character has the key "Name"
    :postcondition: the "Name" key in character has a value of the inputted string
    """
    name = input(rgb(0, 255, 255) + "What's your name?: " + constants.RESET)
    character["Name"] = name


def choose_rod(character: dict) -> str:
    """
    Ask the player which fishing rod they want to use.

    :param character: a dictionary containing the character information
    :precondition: character has the keys: "Stamina", "Max Stamina", and "Fishing Power"
    :precondition: the player inputs something
    :postcondition: if the player inputs "1", the "Stamina" and "Max Stamina" keys have a value of 6 and
                    "Fishing Power" has a value of 4
    :postcondition: if the player inputs "2", the "Stamina" and "Max Stamina" keys have a value of 4 and
                    "Fishing Power" has a value of 6
    :postcondition: if the player does not input "1", "2", the player is prompted to input a valid response
    :return rod: a string of either "Stamina Rod" or "Power Rod" depending on which the player picked
    """
    print(rgb(0, 255, 255) + "Which rod did you pick?: ")
    rod = False
    while rod is False:
        rod = input("\t1 - Stamina Rod\n\t2 - Power Rod\n" + constants.RESET)
        if rod == "1":
            rod = "Stamina Rod"
            character["Stamina"] = 6
            character["Max Stamina"] = 6
            character["Fishing Power"] = 4
        elif rod == "2":
            rod = "Power Rod"
            character["Stamina"] = 4
            character["Max Stamina"] = 4
            character["Fishing Power"] = 6
        elif rod != "1" or rod != "2":
            print(rgb(240, 230, 150) + '"Sorry, I didn\'t quite catch that!"')
            print(rgb(255, 175, 175) + '(Please enter 1 or 2 to select your fishing rod)' + constants.RESET)
            rod = False
    return rod


def make_fish_collection() -> tuple:  # REVISE FISH NAMES AND DESC
    """
    Create a tuple containing a dictionary of the collection of fish you can catch in each area.

    :precondition: player has started the game
    :postcondition: creates a dictionary contain the available fish you can catch for each area of the game
    :postcondition: each dictionary contains a key that is an integer and a tuple containing a string of the fish name
                    and another string of the fish's description
    :postcondition: creates a tuple containing the dictionaries of the collection of fish you can catch in each area
    :return fish_collection_area_one, fish_collection_area_two, fish_collection_area_three, final_fish: four
                    dictionaries contained within a tuple
    >>> fish_collection = make_fish_collection()
    >>> fish_collection == ({1: ('Goldfish', 'BUY GOLD!'), 2: ('Guppy', 'A tiny little fella. A little, little fish.'),
    ... 3: ('Neon Tetra', 'A small fish with a bright line to light up your life.')},
    ... {4: ('Dogfish', 'Weird dog, er-- fish.'), 5: ('Catfish', "It's hissing at you..."),
    ... 6: ('River Trout', 'How does this affect the trout population?')},
    ... {7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this glue doing here?"),
    ... 8: ('Bigfish', "Small in size, but big in heart. It's blue, and it's... incredibly shiny"),
    ... 9: ('Flying Fish', 'It practically flew into your boat!'), 10: ('Shark', 'Doo doo doo, doo doo doo doo doo.')},
    ... {11: ('Final Fishasy', "The legendary fish... and now it's in your bucket.")})
    True
    """
    fish_collection_area_one = {1: ('Goldfish', 'BUY GOLD!'),
                                2: ('Guppy', 'A tiny little fella. A little, little fish.'),
                                3: ('Neon Tetra', 'A small fish with a bright line to light up your life.')}
    fish_collection_area_two = {4: ('Dogfish', 'Weird dog, er-- fish.'),
                                5: ('Catfish', 'It\'s hissing at you...'),
                                6: ('River Trout', 'How does this affect the trout population?')}
    fish_collection_area_three = {7: ('Tuna', "Can't piano a tuna, but you can tuna piano! Hey, what's this glue doing"
                                              " here?"),
                                  8: ('Bigfish',
                                      "Small in size, but big in heart. It's blue, and it's... incredibly shiny"),
                                  9: ('Flying Fish', 'It practically flew into your boat!'),
                                  10: ('Shark', 'Doo doo doo, doo doo doo doo doo.')}
    final_fish = {11: ('Final Fishasy', 'The legendary fish... and now it\'s in your bucket.')}
    return fish_collection_area_one, fish_collection_area_two, fish_collection_area_three, final_fish

