"""
A collection of functions used to simply print scenes and information to the player.
"""
import time
import setup
import user_action
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

    >>> board_test = setup.make_board(3, 3)
    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(board_test, character_test)
    You are currently at (0, 0), Calm Field.

    >>> board_test = setup.make_board(3, 3)
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
        print(f"{number}: {fish[1][0].capitalize()}")
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


def starting_scene(character):
    """
    Prints out a scene when the player gets to the first area.

    :param character:
    :return:
    """
    print('"Hey!"')
    time.sleep(1)
    print('"You!"')
    time.sleep(2)
    print("You look around and a man fully decked out in fish gear catches your eye. You are amazed at his complete "
          "fisher outfit and just how many fish related accessories he has attached to his belt. He enthusiastically "
          "waves at you as he drives his boat next to yours.")
    time.sleep(3)
    print('"Bahahaha! You\'re new here, aren\'tcha."')
    print('"What\'s your name, newbie?"')
    name = setup.get_name(character)
    print(f'"{name}? That\'s a fine name! They call me Marlin."')
    time.sleep(1)
    print("Is that a new fishing rod? It's got that new rod smell. Hey! I know that that brand, which version did you "
          "get?")
    rod = setup.choose_rod(character)
    print(f"The {rod}, eh?")
    if rod == "Stamina Rod":
        print("Good choice! That rod is light and easy on the body. Might not be as powerful but you'll be able to fish"
              " for longer\n[Stamina: 6, Fishing Power: 4]")
    elif rod == "Power Rod":
        print("Good choice! That rod is quite powerful. It's a little heavy, but I'd say catching fish will be a bit "
              "easier.\n[Stamina: 4, Fishing Power: 6]")
    time.sleep(2)
    print(f'So, "{name}, have you fished before?"')
    message_fish = """Input your response:
    1 - No, I'm completely new!
    2 - Yes, but I'm a bit rusty!
    3 - Yes, I'm a pro!
    """
    answer_fish = user_action.get_response(message_fish, 3)
    if answer_fish == 1:
        print('"Bahahaha! A real treat! Don\'t fret, little guppy, I\'ll show you the ropes."')
    elif answer_fish == 2:
        print('"No need to fret, we all need a refresher from time to time!"')
    elif answer_fish == 3:
        print("A pro, eh? Forgive me for assuming yer new! Don't let me hold you up then. Best of luck,", name + "!")
    if answer_fish in {1, 2}:
        # tutorial
        pass


def print_area_scene(character):
    """
    Prints a scene of the player moving to the first area.

    :param character:
    :return:
    """
    if character["Level"] == 1:
        print("\nYou make your way to Initium Lake. A calm lake full of fish. You've heard it was the ideal spot for"
              " beginner fishers (Like you!).")
        print("""
⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

██╗███╗   ██╗██╗████████╗██╗██╗   ██╗███╗   ███╗    ██╗      █████╗ ██╗  ██╗███████╗
██║████╗  ██║██║╚══██╔══╝██║██║   ██║████╗ ████║    ██║     ██╔══██╗██║ ██╔╝██╔════╝
██║██╔██╗ ██║██║   ██║   ██║██║   ██║██╔████╔██║    ██║     ███████║█████╔╝ █████╗  
██║██║╚██╗██║██║   ██║   ██║██║   ██║██║╚██╔╝██║    ██║     ██╔══██║██╔═██╗ ██╔══╝  
██║██║ ╚████║██║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║    ███████╗██║  ██║██║  ██╗███████╗
╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
""")
    elif character["Level"] == 2:
        print("Good luck, " + character["Name"] + ", and enjoy your journey.")
        print("cool ascii art of level 2 area name")
    elif character["Level"] == 3:
        print("Good luck, " + character["Name"] + ", and enjoy your journey.")
        print("cool ascii art of level 3 area name")
    elif character["Level"] == 4:
        print("Good luck, " + character["Name"] + ", and enjoy your journey.")
        print("cool ascii art of level 4 area name")
