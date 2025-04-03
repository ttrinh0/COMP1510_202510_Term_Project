"""
Module of functions that do checks and validations.
"""
import random
import print_or_scene
import time


def process_choice(choice):
    """

    :param choice:
    :return:
    """
    if choice in {"North", "West", "South", "East"}:
        return "Movement"
    else:
        return choice


def validate_move(board, character, direction):
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

    >>> board_test = make_board(3, 3)
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> direction_test = "South"
    >>> validate_move(board_test, character_test, direction_test)
    True

    >>> board_test = make_board(3, 3)
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


def check_for_fish():
    """
    Check to see if a fish is on a space.

    :postcondition: return True if there is an enemy encounter, else return False
    :return True: a Boolean with the value of True if there is an enemy encounter
    :return False: a Boolean with the value of False if there is not an enemy encounter
    """
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
        return False


def check_fish_type(character, complete_fish_collection):
    """
    Return a fish randomly picked from the player's level pool.

    :return:
    """
    level = character["Level"]
    fish_pool = list(complete_fish_collection[level - 1].items())
    fish = random.choice(fish_pool)
    fish_name = fish[1][0]
    print("You caught a(n) " + fish_name + "!")
    return fish


def check_fish_in_collection(character, fish):
    """
    Check to see if fish caught is in the player's fish collection.

    :return:
    """
    fish_number = fish[0]
    character_collection = character["Fish Collection"][fish_number]
    if character_collection == fish[1]:
        return False
    else:
        return True


def check_if_goal_attained(character):
    """
    Check to see if the goal is attained.

    The goal is attained when the character is at the end goal location and their HP is above zero.

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates and the current HP
    :postcondition: return True if the goal is attained, else return False
    :return True: a Boolean with the value of True if the goal is attained
    :return False: a Boolean with the value of False if the direction is valid
    """
    if ('Final Fish', '???') in character["Fish Collection"].values() and character["Stamina"] > 0:
        return True
    else:
        return False

def is_alive(character):
    """
    Return a Boolean signifying whether the character's HP is greater than zero.

    :param character: a dictionary containing the character information
    :precondition: character contains a key called "Current HP" with an integer value of zero or greater
    :postcondition: returns True if the character's current HP is greater than 0, else returns False
    :return True: a Boolean with the value of True if the character's "Current HP" is greater than 0
    :return False: a Boolean with the value of False if the character's "Current HP" is 0

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> is_alive(character_test)
    True

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0}
    >>> is_alive(character_test)
    False
    """
    if character["Stamina"] > 0:
        return True
    else:
        return False


def level_up(character, complete_fish_collection):
    """

    :param character:
    :param complete_fish_collection:
    :return:
    """
    level = character["Level"]
    collection_check = complete_fish_collection[level - 1]
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
    if character["Level"] == 3:
        character["Title"] = "Expert Fisher"
    if character["Level"] == 4:
        character["Title"] = "Legendary Fisher"
    print("Congratulations! You leveled up!\nYou are now level " + str(character["Level"]) + ", " +
          character["Title"] + ".")
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
