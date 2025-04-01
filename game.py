"""
Module info
"""

import just_print
import setup
import check
import random
import time
from color50 import rgb, constants


def get_user_choice():
    """
    Ask the user which direction they would like to move and return the corresponding direction.

    :postcondition: return a string representing the direction the user's input corresponds to
    :return direction: a string representing the direction the user's input corresponds to
    """
    choice = False
    while choice is False:
        print("Enter a Command!\n"
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
    return choice


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


def fishing_game(character, fish):  # Have to add character stats
    """
    """
    level = character["Level"]
    fishing_power = character["Fishing Power"]
    wait_time = random.randint(1, 3)
    fish_reel = random.randint(2, 4)
    # The amount of times you have to do it is determined by the level base - fishing power
    # The higher your fishing power, the fewer times you have to reel
    hooked_wait_time = random.randint(0, 3)
    win_count = 0
    print("You cast your rod.\nInput the specified key within 3 seconds when prompted!")
    for _ in range(wait_time):
        time.sleep(1)
        print("...")
    time.sleep(1)
    print("\nSomething hooks!")
    for _ in range(fish_reel):
        # The keys you need to press will be from 1 to your level + 1
        key = random.randint(1, level + 1)
        start_time = time.time()
        user_input = input(f"><(((º> Input {key}!\n")
        # the time you have to press the key will decrease depending on your level
        if time.time() - start_time > 3.0 and user_input != key:
            character["Stamina"] -= 1
            print("\nThe fish breaks free and gets away...\nYour stamina decreases by 1")
            break
        else:
            print("\tHIT!")
            time.sleep(hooked_wait_time)
            win_count += 1
            continue
    if win_count == fish_reel:
        character["Fish Caught"] += 1


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
    name, user_rod = setup.intro_scene()
    rows = 5
    columns = 5
    board = setup.make_board(rows, columns)
    character = setup.make_character(name, user_rod)
    complete_fish_collection = setup.make_fish_collection()
    achieved_goal = False
    while check.is_alive(character) and not achieved_goal:
        just_print.ascii_board(board, character)
        just_print.describe_current_location(board, character)
        choice = get_user_choice()
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
            just_print.print_player_info(character)
        elif action == "Collection":
            just_print.print_fish_collection(character)
        elif action == "Fish":
            there_is_a_fish = check.check_for_fish()
            if there_is_a_fish:
                fishing_game(character)
                print("\nYou caught the fish!\n")
                just_print.print_fish_collection(character)
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
