"""
Module of functions that set up the game and initial character stats.
"""
import random
from color50 import rgb, constants


def create_game_parameters():
    """

    :return:
    """
    game_parameters = {"Input Time": {1: 3.0, 2: 2.5, 3: 2.0, 4: 1.5}, "Fish Reel": {1: 8, 2: 10, 3: 15, 4: 20},
                       "Event Coordinates One": {(1, 1): "NPC", (4, 3): "NPC", (2, 4): "NPC"},
                       "Event Coordinates Two": {(1, 1): "NPC", (4, 3): "NPC", (2, 4): "NPC"},
                       "Event Coordinates Three": {(1, 1): "NPC", (4, 3): "NPC", (2, 4): "NPC"},
                       "Event Coordinates Final": {(1, 1): "NPC", (4, 3): "NPC", (2, 4): "NPC"}}

    return game_parameters


def make_board(rows, columns, game_parameters, level=1):
    """
    Return a dictionary that contains the coordinates and names of each spot on the game board.

    This function will create a game board with dimensions "rows" by "columns".

    :param game_parameters:
    :param rows: a positive integer greater than zero
    :param columns: a positive integer greater than zero
    :param level: a positive integer between 1 and 4 inclusive, indicating player's level
    :precondition: both rows and columns must be a positive integer
    :precondition: either rows or columns must be greater than one
    :postcondition: a dictionary with keys that are tuples containing the coordinates of the board
    :postcondition: a dictionary with values containing a string representing the name of a game location
    :return coordinates: a dictionary containing key-value pairs that represent the coordinate and name of the game
    location
    """
    coordinates = {}
    room_description = ["", ""]  # random generated square names/descriptions
    for number in range(rows):
        for element in range(columns):
            coordinates[(number, element)] = random.choice(room_description)

    if level == 1:
        for coordinate in game_parameters["Event Coordinates One"]:
            coordinates[coordinate] = game_parameters["Event Coordinates One"][coordinate]

    elif level == 2:  # customization for level 2 map
        for coordinate in game_parameters["Event Coordinates Two"]:
            coordinates[coordinate] = game_parameters["Event Coordinates Two"][coordinate]

    elif level == 3:  # customization for level 3 map
        for coordinate in game_parameters["Event Coordinates Three"]:
            coordinates[coordinate] = game_parameters["Event Coordinates Three"][coordinate]

    elif level == 4:  # customization for boss map
        for coordinate in game_parameters["Event Coordinates Final"]:
            coordinates[coordinate] = game_parameters["Event Coordinates Final"][coordinate]

    return coordinates


def add_on_board(character):
    """
    Place NPCs and other visible objects onto the board depending on the player's level.

    :param character: a dictionary containing the player's information
    :return:
    """
    pass


def make_character():  # REDO DIALOGUE
    """
    Return a dictionary containing a character's starting coordinates and HP.

    :postcondition: return a dictionary with keys: "Name", "Stamina", "Fishing Power", "X-coordinate", "Y-coordinate"
    :return: a dictionary containing character information
    """
    character_profile = {"X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Title": "Beginner Fisher", "Name": "",
                         "Stamina": 1, "Max Stamina": 1, "Fishing Power": 1, "Fish Caught": 0, "Fish Limit": 0,
                         "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"), 4: ("???", "???"),
                                             5: ("???", "???"), 6: ("???", "???"), 7: ("???", "???"), 8: ("???", "???"),
                                             9: ("???", "???"), 10: ("???", "???"), 11: ("???", "???")}}
    return character_profile


def get_name(character):
    """
    Ask the player for their name.

    :param character: a dictionary with the character information
    :precondition: the player inputs a name (or any string/value)
    :precondition: character has the key "Name"
    :postcondition: the "Name" key in character has a value of the inputted string
    :return name: a string of the player's inputted name
    """
    name = input(rgb(0, 255, 255) + "What's your name?: " + constants.RESET)
    character["Name"] = name
    return name


def choose_rod(character):
    """
    Ask the player which fishing rod they want to use.

    :precondition: the player inputs 1 or 2
    :postcondition:
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


def make_fish_collection():  # REVISE FISH NAMES AND DESC
    """
    Create a tuple containing a dictionary of the collection of fish you can catch in each area.

    :precondition: player has started the game
    :postcondition: creates a dictionary contain the available fish you can catch for each area of the game
    :postcondition: each dictionary contains a key that is an integer and a tuple containing a string of the fish name
                    and another string of the fish's description
    :postcondition: creates a tuple containing the dictionaries of the collection of fish you can catch in each area
    :return fish_collection_area_one, fish_collection_area_two, fish_collection_area_three, final_fish: four
                    dictionaries contained within a tuple
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

