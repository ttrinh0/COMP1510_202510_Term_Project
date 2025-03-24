"""
Module info
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


def game():
    """
    Drive the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
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
                guessing_game(character)
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
