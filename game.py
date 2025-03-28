"""
Module info
"""

import random
import time
from table2ascii import table2ascii, PresetStyle


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
            board_rows[number].append(" ")
    board_rows[character_position_y][character_position_x] = "x"

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
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
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
