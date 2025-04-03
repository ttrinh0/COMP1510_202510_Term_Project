"""
Module info
"""

import print_or_scene
import setup
import check
import user_action
import time
from color50 import rgb, constants


def move_character(character, direction):
    """
    Change the character's coordinates depending on direction value.

    :param character: a dictionary containing the character information
    :param direction: a string containing the direction the user wants to move
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :precondition: direction must be a string with a value of either "East", "West", "South", "North"
    :postcondition: changes the user coordinates depending on direction

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> direction_test = "South"
    >>> move_character(character_test, direction_test)
    >>> print(character_test)
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}

    >>> character_test = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> direction_test = "North"
    >>> move_character(character_test, direction_test)
    >>> print(character_test)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    """
    if direction == "North":
        character["Y-coordinate"] -= 1
    elif direction == "South":
        character["Y-coordinate"] += 1
    elif direction == "East":
        character["X-coordinate"] += 1
    elif direction == "West":
        character["X-coordinate"] -= 1


def add_fish_to_collection(character, fish):
    """
    Add fish into player collection.

    :param character:
    :param fish:
    :return:
    """
    fish_number = fish[0]
    player_collection = character["Fish Collection"]
    player_collection[fish_number] = fish[1]


def game():
    """
    Drive the game.
    """
    rows = 5
    columns = 5
    name, user_rod = setup.intro_scene()
    board = setup.make_board(rows, columns)
    character = setup.make_character(name, user_rod)
    complete_fish_collection = setup.make_fish_collection()
    game_parameters = setup.create_game_parameters()
    achieved_goal = False
    print_or_scene.print_area_scene(character)
    print_or_scene.starting_scene(character)
    while check.is_alive(character) and not achieved_goal:
        print_or_scene.ascii_board(board, character)
        print_or_scene.describe_current_location(board, character)
        choice = user_action.get_user_choice()
        action = check.process_choice(choice)
        if action == "Movement":
            valid_move = check.validate_move(board, character, choice)
            if valid_move:
                move_character(character, choice)
                achieved_goal = check.check_if_goal_attained(character)
            else:
                print(rgb(255, 175, 175) + "You can't move there! Pick another direction." + constants.RESET)
        elif action == "Interact":
            pass
        # Create function to check if there's something on the map
        # If yes, print text/dialogue
        elif action == "Profile":
            print_or_scene.print_player_info(character)
        elif action == "Collection":
            print_or_scene.print_fish_collection(character)
        elif action == "Fish":
            there_is_a_fish = check.check_for_fish()
            if there_is_a_fish:
                win = user_action.fishing_game(character, game_parameters)
                if win:
                    fish = check.check_fish_type(character, complete_fish_collection)
                    if check.check_fish_in_collection(character, fish):
                        add_fish_to_collection(character, fish)
                        check.level_up(character, complete_fish_collection)
                        check.final_conditions(character)
                print_or_scene.print_fish_collection(character)
                print()
                time.sleep(1)
    if achieved_goal:
        print(rgb(255, 255, 0) + "You made it to the end! Congratulations!" + constants.RESET)
    else:
        print("Game Over.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
