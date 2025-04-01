"""
Module info
"""

import random
import time
from table2ascii import table2ascii, PresetStyle
from color50 import rgb, constants


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
    character_profile = {"X-coordinate": 0, "Y-coordinate": 0, "Level": 1, "Character": "Beginner Fisher", "Name": name}

    if user_rod == "Stamina Rod":
        character_profile["Stamina"] = 6
        character_profile["Fishing Power"] = 4
    if user_rod == "Power Rod":
        character_profile["Stamina"] = 4
        character_profile["Fishing Power"] = 6

    return character_profile


def make_fish_collection():  # REVISE FISH NAMES AND DESC
    """
    Creates a dictionary of the fish you can catch in each area.

    :return:
    """
    fish_collection_area_one = {"1. fish": "fish desc", "2. fish": "fish desc", "3. fish": "fish desc"}
    fish_collection_area_two = {"4. fish": "fish desc", "5. fish": "fish desc", "6. fish": "fish desc"}
    fish_collection_area_three = {"7. fish7": "fish desc", "8. fish": "fish desc", "9. fish": "fish desc",
                                  "10. fish": "fish desc"}

    return fish_collection_area_one, fish_collection_area_two, fish_collection_area_three


def make_player_fish_collection():
    """
    Create a dictionary representing the fish the player has caught.

    :return:
    """
    fish_collection = {"1. ???": "???", "2. ???": "???", "3. ???": "???", "4. ???": "???", "5. ???": "???",
                       "6. ???": "???", "7. ???": "???", "8. ???": "???", "9. ???": "???", "10. ???": "???", }
    return fish_collection


def ascii_board(board, character):
    """
    Print the game board using ascii.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs
    :postcondition: prints the game board including the character's location and the end goal location
    """
    board_rows = []
    board_spaces = []
    character_position_x = character["X-coordinate"]
    character_position_y = character["Y-coordinate"]
    rows = max(board)[0] + 1
    columns = max(board)[1] + 1
    for number in range(rows):
        board_rows.append(board_spaces.copy())
        for element in range(columns):
            board_rows[number].append("  ")
    board_rows[character_position_y][character_position_x] = "⛵"

    output = table2ascii(
        body=board_rows,
        style=PresetStyle.ascii_box
    )
    print(output)


def describe_current_location(board, character):
    """
    Print the character's current coordinates and the game board.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :postcondition: prints the character's current coordinates and the ascii game board

    >>> board_test = make_board(3, 3)
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(board_test, character_test)
    You are currently at (0, 0), Calm Field.

    >>> board_test = make_board(3, 3)
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
    >>> describe_current_location(board_test, character_test)
    You are currently at (2, 2), The End.
    """
    current_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    location_description = board[current_coordinates]
    message = "You are currently at " + str(current_coordinates) + ", " + location_description + "."
    print(message)


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


def process_choice(choice):
    """

    :param choice:
    :return:
    """
    if choice in {"North", "West", "South", "East"}:
        return "Movement"
    elif choice == "Fish":
        return choice
    elif choice == "Interact":
        return choice
    elif choice == "Profile":
        return "Account"
    elif choice == "Collection":
        return "Account"


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


def check_if_goal_attained(board, character):
    """
    Check to see if the goal is attained.

    The goal is attained when the character is at the end goal location and their HP is above zero.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates and the current HP
    :postcondition: return True if the goal is attained, else return False
    :return True: a Boolean with the value of True if the goal is attained
    :return False: a Boolean with the value of False if the direction is valid

    >>> board_test = make_board(3, 3)
    >>> character_test = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> check_if_goal_attained(board_test, character_test)
    False

    >>> board_test = make_board(3, 3)
    >>> character_test = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
    >>> check_if_goal_attained(board_test, character_test)
    True
    """
    if (character["X-coordinate"], character["Y-coordinate"]) == max(board) and character["Current HP"] > 0:
        return True
    else:
        return False


def check_for_foes(board, character):
    """
    Check to see if an enemy is on a space.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :postcondition: return True if there is an enemy encounter, else return False
    :return True: a Boolean with the value of True if there is an enemy encounter
    :return False: a Boolean with the value of False if there is not an enemy encounter
    """
    enemy_encounter = random.randint(1, 4)
    if (character['X-coordinate'], character['Y-coordinate']) != max(board):
        if enemy_encounter == 1:
            return True
        else:
            return False


def fishing_game():  # Have to add character stats
    """
    """
    wait_time = random.randint(1, 3)
    fish_reel = random.randint(2, 4)
    # The amount of times you have to do it is determined by the level base - fishing power
    # The higher your fishing power, the fewer times you have to reel
    hooked_wait_time = random.randint(0, 3)
    win_count = 0
    print("You cast your rod.")

    for _ in range(wait_time):
        time.sleep(1)
        print("...")
    time.sleep(1)
    print()
    print("Something hooks! Input the specified key within 3 seconds when prompted!")
    for _ in range(fish_reel):
        # The keys you need to press will be from 1 to your level + 1
        key = random.randint(1, 2)
        start_time = time.time()
        user_input = input(f"><(((º> Press {key}!\n")
        # the time you have to press the key will decrease depending on your level
        if time.time() - start_time > 3.0 or user_input != str(key):
            print("The fish breaks free and gets away...")
            print("Your stamina decreases by 1")
            break
        else:
            time.sleep(hooked_wait_time)
            win_count += 1
            continue
    if win_count == fish_reel:
        print("You caught the fish!")


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


def game():
    """
    Drive the game.
    """
    name, user_rod = intro_scene()
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character(name, user_rod)
    achieved_goal = False
    describe_current_location(board, character)
    ascii_board(board, character)
    while is_alive(character) and not achieved_goal:
        choice = get_user_choice()
        action = process_choice(choice)
        if action == "Movement":
            valid_move = validate_move(board, character, choice)
            if valid_move:
                move_character(character, choice)
                describe_current_location(board, character)
                ascii_board(board, character)
                there_is_a_challenger = check_for_foes(board, character)
                if there_is_a_challenger:
                    fishing_game(character)
                achieved_goal = check_if_goal_attained(board, character)
            else:
                print(rgb(255, 175, 175) + "You can't move there! Pick another direction." + constants.RESET)
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
