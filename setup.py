"""

"""
import random


def make_board(rows, columns, level=1):
    """
    Return a dictionary that contains the coordinates and names of each spot on the game board.

    This function will create a game board with dimensions "rows" by "columns".

    :param rows: a positive integer greater than zero
    :param columns: a positive integer greater than zero
    :param level: a positive integer between 1 and 4 inclusive, indicating player's level
    :precondition: both rows and columns must be a positive integer
    :precondition: either rows or columns must be greater than one
    :postcondition: a dictionary with keys that are tuples containing the coordinates of the board
    :postcondition: a dictionary with values containing a string representing the name of a game location
    :return coordinates: a dictionary containing key-value pairs that represent the coordinate and name of the game location
    """
    coordinates = {}
    room_description = ["", ""]  # random generated square names/descriptions
    for number in range(rows):
        for element in range(columns):
            coordinates[(number, element)] = random.choice(room_description)
    coordinates[(0, 0)] = ""  # if the start needs to have a specific name
    coordinates[(rows - 1, columns - 1)] = ""  # if there's an end point

    if level == 2:  # customization for level 2 map
        pass

    if level == 3:  # customization for level 3 map
        pass

    if level == 4:  # customization for boss map
        pass

    return coordinates


def intro_scene():
    """
    Print an intro scene and return the inputted name and chosen fishing rod of the player.

    """
    print("You wake up, excited. Today is the day you will begin your journey.")
    name = input("Enter your name: ")
    print("something about going to the fishing ")
    print("Which rod would you like to start with: ")
    user_rod = False
    while user_rod is False:
        user_rod = input("1. Stamina Rod\n2. Power Rod\n")
        if user_rod == "1":
            user_rod = "Stamina Rod"
        elif user_rod == "2":
            user_rod = "Power Rod"
        elif user_rod != "1" or user_rod != "2":
            print("Please enter 1 or 2 to select your fishing rod")
            user_rod = False
    return name, user_rod


def make_character(name, user_rod):  # REDO DIALOGUE
    """
    Return a dictionary containing a character's starting coordinates and HP.

    :postcondition: return a dictionary with keys: "Name", "Stamina", "Fishing Power", "X-coordinate", "Y-coordinate"
    :return: a dictionary containing character information
    """
    character_profile = {"X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Title": "Beginner Fisher", "Name": name,
                         "Fish Caught": 0, "Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"),
                                                               4: ("???", "???"),
                                                               5: ("???", "???"), 6: ("???", "???"), 7: ("???", "???"),
                                                               8: ("???", "???"),
                                                               9: ("???", "???"), 10: ("???", "???")}}
    if user_rod == "Stamina Rod":
        character_profile["Stamina"] = 6
        character_profile["Max Stamina"] = 6
        character_profile["Fishing Power"] = 4
    if user_rod == "Power Rod":
        character_profile["Stamina"] = 4
        character_profile["Max Stamina"] = 4
        character_profile["Fishing Power"] = 6

    return character_profile


def make_fish_collection():  # REVISE FISH NAMES AND DESC
    """
    Creates a dictionary for the collection of fish you can catch in each area.

    :return:
    """
    fish_collection_area_one = {1: ('fish name', 'fish desc'), 2: ('fish name', 'fish desc'), 3: ('fish name', 'fish desc')}
    fish_collection_area_two = {4: ('fish name', 'fish desc'), 5: ('fish name', 'fish desc'), 6: ('fish name', 'fish desc')}
    fish_collection_area_three = {7: ('fish name', 'fish desc'), 8: ('fish name', 'fish desc'), 9: ('fish name', 'fish desc'), 10: ('fish name', 'fish desc')}

    return fish_collection_area_one, fish_collection_area_two, fish_collection_area_three