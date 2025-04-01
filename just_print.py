"""
A collection of functions used to simply print scenes and information to the player.
"""
from table2ascii import table2ascii, PresetStyle


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


def print_fish_collection(character):
    """
    Print the player's fish collection.
    :param character:
    """
    fish_list = sorted(character["Fish Collection"].items())
    print("\tFish Collection")
    print("-" * 23)
    for number, fish in enumerate(fish_list, 1):
        print(f"{number}: {fish[1][0]}")
    print("-" * 23)


def print_player_info(character):
    """
    Print the player's information.
    :param character:
    """
    print("\tPlayer Information")
    print("-" * 26)
    print("Name: " + character["Name"] +
          "\nTitle: " + character["Title"] +
          "\nLevel: " + str(character["Level"]) +
          "\nStamina: " + str(character["Stamina"]) + "/" + str(character["Max Stamina"]) +
          "\nFishing Power: " + str(character["Fishing Power"]) +
          "\nFish Caught: " + str(character["Fish Caught"]))
    print("-" * 26)