"""
Module of functions that do checks and validations.
"""
import random
import print_or_scene
import setup
from color50 import rgb, constants
import time


def process_choice(choice: str) -> str:
    """
    Determine if the player entered a direction or another option.

    :precondition: choice is a string
    :param choice:
    :postcondition: returns "Movement" if the choice is one of the cardinal directions
    :postcondition: returns choice if the choice is not one of the cardinal directions
    :return: the string, "Movement", if the choice is one of the cardinal directions
    :return choice: the string that is passed through the function if the choice is not one of the cardinal directions

    >>> process_choice("North")
    'Movement'
    >>> process_choice("Fish")
    'Fish'
    """
    if choice in {"North", "West", "South", "East"}:
        return "Movement"
    else:
        return choice


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Check the direction to see if it is a valid move.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :param direction: a string containing the direction the user wants to move
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :precondition: direction must be a string with a value of either "East", "West", "South", "North"
    :postcondition: return True if the direction is valid, else return False
    :return True: a Boolean with the value of True if the direction is valid
    :return False: a Boolean with the value of False if the direction is valid

    >>> board_test = setup.make_board(3, 3)
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> direction_test = "South"
    >>> validate_move(board_test, character_test, direction_test)
    True

    >>> board_test = setup.make_board(3, 3)
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> direction_test = "West"
    >>> validate_move(board_test, character_test, direction_test)
    False
    """
    character_position = (character["X-coordinate"], character["Y-coordinate"])
    if character_position[0] < max(board)[0] and direction == "East":
        return True
    elif character_position[0] > min(board)[0] and direction == "West":
        return True
    elif character_position[1] < max(board)[1] and direction == "South":
        return True
    elif character_position[1] > min(board)[1] and direction == "North":
        return True
    else:
        return False


def check_for_fish(character: dict) -> bool | None:
    """
    Check to see if a fish is on a space.

    :param character: a dictionary containing the character information
    :precondition: character is a dictionary with the key "Fish Limit"
    :postcondition: prints "Nothing's biting. It might be time to move to another spot." if the key "Fish Limit"
                    in character has a value of 3 or greater
    :postcondition: prints "Nothing's biting." if "Fish Limit is less than 3 and there is not a fish encounter
    :postcondition: return True if there is a fish encounter
    :return True: a Boolean with the value of True if there is a fish encounter
    """
    if character["Fish Limit"] < 3:
        character["Fish Limit"] += 1
        enemy_encounter = random.randint(1, 3)
        if enemy_encounter != 1:
            return True
        else:
            print("You cast your rod.")
            for _ in range(2):
                print("...")
                time.sleep(1)
            print("Nothing's biting.")
            time.sleep(1)
    else:
        print("You cast your rod.")
        for _ in range(2):
            print("...")
            time.sleep(1)
        print("Nothing's biting. It might be time to move to another spot.")


def check_fish_type(character: dict, complete_fish_collection: tuple) -> tuple:
    """
    Return a fish randomly picked from the specific area the player is in.

    :param character: a dictionary containing the character information
    :param complete_fish_collection: a tuple containing four dictionaries of the fish the player can catch in each area
    :precondition: character has the key "Level"
    :precondition: complete_fish_collection contains four dictionaries of the fish the player can catch in each area
    :postcondition: prints a statement telling the player which fish they caught and its description
    :postcondition: randomly selects a fish tuple from the fish collection of the area the player is in and returns it
    :return fish: a tuple that has a fish's number and another tuple containing the fish's name and description
    """
    level = character["Level"]
    fish_pool = list(complete_fish_collection[level - 1].items())
    fish = random.choice(fish_pool)
    fish_name = fish[1][0]
    print(rgb(200, 250, 255) + "You caught a(n) " + fish_name + "!")
    print(rgb(100, 200, 255) + r"""      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´ """)
    print(rgb(200, 250, 255) + fish[1][1] + constants.RESET)
    return fish


def check_fish_in_collection(character: dict, fish: tuple) -> bool:
    """
    Check to see if fish caught is in the player's fish collection.

    :param character: a dictionary containing the character information
    :param fish: a tuple that has a fish's number and another tuple containing the fish's name and description
    :precondition: character contains the key "Fish Collection"
    :precondition: fish is a tuple that has a fish's number and another tuple containing the fish's name and description
    :postcondition: returns True is the fish is not in the player's fish collection, else returns False
    :return False: if the fish is in the player's fish collection
    :return True: if the fish is not in the player's fish collection

    >>> character_test = {"Fish Collection": {1: ("???", "???"), 2: ("???", "???"), 3: ("???", "???"), 4: ("???", "???"),
    ...                                      5: ("???", "???"), 6: ("???", "???"), 7: ("???", "???"), 8: ("???", "???"),
    ...                                      9: ("???", "???"), 10: ("???", "???"), 11: ("???", "???")}}
    >>> fish_test = (1, ('Goldfish', 'BUY GOLD!'))
    >>> check_fish_in_collection(character_test, fish_test)
    True
    >>> character_test = {"Fish Collection": {1: ('Goldfish', 'BUY GOLD!'), 2: ("???", "???"), 3: ("???", "???"),
    ...                                       4: ("???", "???"), 5: ("???", "???"), 6: ("???", "???"),
    ...                                       7: ("???", "???"), 8: ("???", "???"), 9: ("???", "???"),
    ...                                       10: ("???", "???"), 11: ("???", "???")}}
    >>> fish_test = (1, ('Goldfish', 'BUY GOLD!'))
    >>> check_fish_in_collection(character_test, fish_test)
    False
    """
    fish_number = fish[0]
    character_collection = character["Fish Collection"][fish_number]
    if character_collection == fish[1]:
        return False
    else:
        return True


def check_if_goal_attained(character: dict) -> bool:
    """
    Check to see if the goal is attained.

    The goal is attained when the character is level 5 and their stamina is above zero.

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :precondition: character must contain keys "Level" and "Stamina"
    :postcondition: return True if the goal is attained, else return False
    :return True: a Boolean with the value of True if the goal is attained
    :return False: a Boolean with the value of False if the goal is not attained

    >>> character_test = {"Level": 1, "Stamina": 5}
    >>> check_if_goal_attained(character_test)
    False
    >>> character_test = {"Level": 5, "Stamina": 5}
    >>> check_if_goal_attained(character_test)
    True
    """
    if character["Level"] == 5 and character["Stamina"] > 0:
        return True
    else:
        return False


def is_alive(character: dict) -> bool:
    """
    Return a Boolean signifying whether the character's HP is greater than zero.

    :param character: a dictionary containing the character information
    :precondition: character contains a key called "Stamina" with an integer value of zero or greater
    :postcondition: returns True if the character's Stamina is greater than 0, else returns False
    :return True: a Boolean with the value of True if the character's "Stamina" is greater than 0
    :return False: a Boolean with the value of False if the character's "Stamina" is 0

    >>> character_test = {"Stamina": 5}
    >>> is_alive(character_test)
    True

    >>> character_test = {"Stamina": 0}
    >>> is_alive(character_test)
    False
    """
    if character["Stamina"] > 0:
        return True
    else:
        return False


def level_up(character, complete_fish_collection):
    """
    Increase the player's level and stats if the player has caught all the fish in an area.

    At each level, the player's title will also change.

    :param character: a dictionary containing the character information
    :param complete_fish_collection:
    :return:
    """
    collection_check = complete_fish_collection[character["Level"] - 1]
    player_collection = character["Fish Collection"]
    fish_numbers = list(collection_check)
    for fish in fish_numbers:
        if player_collection[fish] != collection_check[fish]:
            return False
    character["Level"] += 1
    character["Stamina"] += 1
    character["Max Stamina"] += 1
    character["Fishing Power"] += 1
    if character["Level"] == 2:
        character["Title"] = "Adept Fisher"
    elif character["Level"] == 3:
        character["Title"] = "Expert Fisher"
    elif character["Level"] == 4:
        character["Title"] = "Legendary Fisher"
    if character["Level"] != 5:
        print(
            "Congratulations! You leveled up!\nYou are now level " + str(character["Level"]) + ", " + character["Title"]
            + ".")
    if character["Level"] == 5:
        print("You did it! You caught it!")
    input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
    print_or_scene.print_area_scene(character)
    return True


def final_conditions(character):
    """

    :param character:
    :return:
    """
    if character["Level"] == 4:
        return True
    else:
        return False
