"""
Module of functions that either take user input or change the player's stats
"""
import time
from color50 import rgb, constants
import random


def get_user_choice():
    """
    Ask the user which direction they would like to move and return the corresponding direction.

    :postcondition: return a string representing the direction the user's input corresponds to
    :return direction: a string representing the direction the user's input corresponds to
    """
    choice = False
    while choice is False:
        print(rgb(150, 255, 230) + "Enter a Command!\n" + constants.RESET +
              "Movement:\t\tAction:\t\t\tCharacter:\n"
              "W - North\t\t1 - Fish\t\t3 - Character Profile\n"
              "A - West\t\t2 - Interact\t4 - Fish Collection\n"
              "S - South\n"
              "D - East")
        user_input = input(rgb(0, 255, 255) + "Type your command here: " + constants.RESET)
        if user_input.strip().lower() == "w":
            choice = "North"
        elif user_input.strip().lower() == "a":
            choice = "West"
        elif user_input.strip().lower() == "s":
            choice = "South"
        elif user_input.strip().lower() == "d":
            choice = "East"
        elif user_input.strip() == "1":
            choice = "Fish"
        elif user_input.strip() == "2":
            choice = "Interact"
        elif user_input.strip() == "3":
            choice = "Profile"
        elif user_input.strip() == "4":
            choice = "Collection"
        else:
            choice = False
            print(rgb(255, 175, 175) + "Please enter a valid option!" + constants.RESET)
    return choice


def fishing_game(character, game_parameters):  # Have to add character stats
    """
    Execute a fishing mini-game.

    The user inputs the specified key a randomly determined amount of times.

    :param game_parameters: a dictionary containing the game parameters
    :param character: a dictionary containing the character information
    :precondition: user input must input a key
    :precondition: character must be a dictionary
    :precondition: character must contain the keys "Stamina", "Fishing Power", "Level", and "Fish Caught", all with
                   values of integers
    :postcondition: decreases the character's stamina by one if the user loses the game
    :postcondition: does not alter character's stamina if the user wins the game
    :postcondition: increases the character's Fish Caught count if the user wins the game
    :postcondition: prints "HIT!" when the user correctly inputs a key
    :postcondition: prints a statement that the fish gets away and the character's stamina decreases if the user loses
                    the game
    :postcondition: prints "Gotcha!" if the user wins the game
    :return False: a Boolean with the value of False if character loses the mini-game
    :return True: a Boolean with the value of True if character wins the mini-game
    """
    # set up the parameters
    level = character["Level"]
    fishing_power = character["Fishing Power"]
    input_time = game_parameters["Input Time"][level]
    fish_reel_constraints = game_parameters["Fish Reel"][level]
    wait_time = random.randint(1, 4)
    fish_reel = random.randint(level, fish_reel_constraints - fishing_power)
    win_count = 0
    print(f"You cast your rod.\nInput the specified key within {input_time} seconds when prompted!")
    for _ in range(wait_time):
        time.sleep(1)
        print("...")
    time.sleep(1)
    # The gameplay
    print("\nSomething hooks!")
    for _ in range(fish_reel):
        # The keys you need to press will be from 1 to your level + 1
        key = random.randint(1, level + 1)
        start_time = time.time()
        user_input = input(rgb(0, 255, 255) + f"><(((º> Input {key}!\n" + constants.RESET)
        # the time you have to press the key will decrease depending on your level
        if time.time() - start_time > input_time or user_input != str(key):
            character["Stamina"] -= 1
            print("\nThe fish breaks free and gets away...\n"
                  "Your stamina decreases by 1\n"
                  "Current stamina:", character["Stamina"])
            return False
        else:
            print(rgb(255, 255, 0) + "\tHIT!" + constants.RESET)
            time.sleep(random.randint(0, 3))
            win_count += 1
            continue
    if win_count == fish_reel:
        character["Fish Caught"] += 1
        print("Gotcha!")
        return True


def move_character(character, direction):
    """
    Change the character's coordinates depending on direction value.

    :param character: a dictionary containing the character information
    :param direction: a string containing the direction the player wants to move
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :precondition: character must contain a key of "Fish Limit"
    :precondition: direction must be a string with a value of either "East", "West", "South", "North"
    :postcondition: changes the player's coordinates depending on direction
    :postcondition: the key "Fish Limit" in the character dictionary has a value of zero

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Fish Limit": 0}
    >>> direction_test = "South"
    >>> move_character(character_test, direction_test)
    >>> print(character_test)
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5, 'Fish Limit': 0}

    >>> character_test = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Fish Limit": 1}
    >>> direction_test = "North"
    >>> move_character(character_test, direction_test)
    >>> print(character_test)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5, 'Fish Limit': 0}
    """
    if direction == "North":
        character["Y-coordinate"] -= 1
    elif direction == "South":
        character["Y-coordinate"] += 1
    elif direction == "East":
        character["X-coordinate"] += 1
    elif direction == "West":
        character["X-coordinate"] -= 1
    character["Fish Limit"] = 0


def add_fish_to_collection(character, fish):
    """
    Add fish into player collection.

    :param character: a dictionary containing the character information
    :param fish: a tuple containing a fish's number and another tuple with its name and description
    :precondition: fish is not in the "Fish Collection" dictionary
    :precondition: character must contain the key "Fish Collection" with the value of a dictionary with
    keys from 1 to 11 that have values that are tuples that either contain "???" or specific fish name and description
    :postcondition: adds the fish the player caught to their fish collection

    >>> character_test = {'Fish Collection': {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"), 4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"), 7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"), 10: ("???", "???"), 11: ("???", "???")}}
    >>> fish_test = (2, ('Guppy', 'A tiny little fella. A little, little fish.'))
    >>> add_fish_to_collection(character_test, fish_test)
    >>> print(character_test)
    {'Fish Collection': {1: ('???', '???'), 2: ('Guppy', 'A tiny little fella. A little, little fish.'), 3: ('???', '???'), 4: ('???', '???'), 5: ('???', '???'), 6: ('???', '???'), 7: ('???', '???'), 8: ('???', '???'), 9: ('???', '???'), 10: ('???', '???'), 11: ('???', '???')}}
    """
    fish_number = fish[0]
    player_collection = character["Fish Collection"]
    player_collection[fish_number] = fish[1]


def get_response(message: str, options: int, option_quit=False):
    """
    Creates a selection input for the player and returns the number the player inputs.

    :param message: a string of the message that is asked or stated to the player
    :param options: a positive integer of one or greater
    :param option_quit: an optional Boolean of True or False
    :precondition: message is a string
    :precondition: options is a positive integer of one or greater
    :precondition: if included, option_quit is a Boolean of True or False
    :precondition: if option_quit not included, option_quit is False
    :postcondition: the user's input is returned if it is valid, else they have to input again until it is
    :return user_input: a string containing the number that represents the player's choice
    """
    response = False
    user_options = [str(number) for number in range(1, options + 1)]
    if option_quit:
        user_options.append("q")
    while response is False:
        user_input = input(message)
        if user_input.lower().strip() in user_options:
            response = user_input
            return response
        else:
            print(rgb(255, 175, 175) + "Please enter a valid option!" + constants.RESET)
