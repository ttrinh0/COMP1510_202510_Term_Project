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


def area_one_scene(character):
    """
    Prints out a scene when the player gets to the first area.

    :param character:
    :return:
    """
    print('"Hey!"')
    time.sleep(1)
    print('"You!"')
    time.sleep(2)
    print("You look around and a man fully decked out in fish gear catches your eye.You are amazed at his complete\n"
          "fisher outfit and just how many fish related accessories he has attached to his belt.")
    time.sleep(1)
    print("He enthusiastically waves at you as he drives his boat next to yours.")
    time.sleep(3)
    print('"Bahahaha! You\'re new here, aren\'tcha."')
    print('"What\'s your name, newbie?"')
    name = setup.get_name(character)
    print(f'"{name}? That\'s a fine name! They call me Marlin."')
    time.sleep(1)
    print("Is that a new fishing rod? It's got that new rod smell.")
    time.sleep(1)
    print("Hey! I know that that brand, which version did you get?")
    rod = setup.choose_rod(character)
    print(f"The {rod}, eh?")
    if rod == "Stamina Rod":
        print("Good choice! That rod is light and easy on the body. Might not be as powerful but you'll be able to fish"
              " for longer\n[Stamina: 6, Fishing Power: 4]")
    elif rod == "Power Rod":
        print("Good choice! That rod is quite powerful. It's a little heavy, but I'd say catching fish will be a bit "
              "easier.\n[Stamina: 4, Fishing Power: 6]")
    time.sleep(2)
    print(f'So, "{name}, you need some pointers?"')
    message_fish = """Input your response:
    1 - Yes please!
    2 - No thanks! I can figure it out!
    """
    answer_fish = user_action.get_response(message_fish, 2)
    if answer_fish == 1:
        print('"Bahahaha! Don\'t fret, little guppy, I\'ll show you the ropes."')
        print_fishing_demo()
    elif answer_fish == 2:
        print('Well, don\'t let me hold you up then. Best of luck,", name + "!"')


def print_fishing_demo():
    """
    Print a tutorial for the fishing minigame.

    :postcondition: prints the tutorial for the minigame
    """
    repeat = False
    while not repeat:
        time.sleep(1)
        print('"Listen here and pay attention, my friend"')
        time.sleep(2)
        print('He takes his fishing rod and gracefully casts it into the lake.')
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("\nSomething hooks!")
        time.sleep(1)
        print('"This is where the challenge really begins!"')
        time.sleep(2)
        print('"You\'ll feel a tug, each time you feel it. You\'re gonna wanna reel and pull it back!"')
        print("[A message will pop up, prompting you to input a key.]")
        print('[><(((º> Input 2!]')
        time.sleep(1)
        print('[When you see this message, input the number you see. In this case, enter 2.]')
        print('"And don\'t let your mind wander! If you\'re too slow, the fish will get away!"')
        print('[If you\'re successful, you\'ll get a "HIT!" message]')
        time.sleep(1)
        print("\tHIT!")
        time.sleep(2)
        print('"You\'ll have to do this a couple times before you\'re able to catch the fish."')
        print('"I think that\'s about all from me. Do you need me to go over it again?"')
        repeat_message = """
        Would you like to see the tutorial again?:
        1 - No
        2 - Yes"""
        repeat = user_action.get_response(repeat_message, 2)
        if repeat == 1:
            print("He nods.")
            print("You'll run into some more challenging fish as you go on your fisher journey.\n"
                  "Bet you're also looking to catch the Final Fishtasy, eh?")
            repeat = True
        elif repeat == 2:
            print('"You need to hear it again? Alrighty."')
            repeat = False


def print_area_scene(character):
    """
    Prints a scene of the player moving to the first area.

    :param character:
    :return:
    """
    if character["Level"] == 1:
        print("\nYou make your way to Initium Pond. A calm pond full of fish.")
        print("""
⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

██╗███╗   ██╗██╗████████╗██╗██╗   ██╗███╗   ███╗    ██████╗  ██████╗ ███╗   ██╗██████╗ 
██║████╗  ██║██║╚══██╔══╝██║██║   ██║████╗ ████║    ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗
██║██╔██╗ ██║██║   ██║   ██║██║   ██║██╔████╔██║    ██████╔╝██║   ██║██╔██╗ ██║██║  ██║
██║██║╚██╗██║██║   ██║   ██║██║   ██║██║╚██╔╝██║    ██╔═══╝ ██║   ██║██║╚██╗██║██║  ██║
██║██║ ╚████║██║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║    ██║     ╚██████╔╝██║ ╚████║██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                                                                                       
⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
""")
    elif character["Level"] == 2:
        print("\nYou go to the Medius River, like Marlin suggested.")
        print("""
 ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

███╗   ███╗███████╗██████╗ ██╗██╗   ██╗███████╗    ██████╗ ██╗██╗   ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗██║██║   ██║██╔════╝    ██╔══██╗██║██║   ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║  ██║██║██║   ██║███████╗    ██████╔╝██║██║   ██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║  ██║██║██║   ██║╚════██║    ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗██████╔╝██║╚██████╔╝███████║    ██║  ██║██║ ╚████╔╝ ███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
 ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
""")
    elif character["Level"] == 3:
        print("\nYou take the trek to Ferefini Ocean.")
        print("""
  ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
███████╗███████╗██████╗ ███████╗███████╗██╗███╗   ██╗██╗     ██████╗  ██████╗███████╗ █████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║████╗  ██║██║    ██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╗  █████╗  ██████╔╝█████╗  █████╗  ██║██╔██╗ ██║██║    ██║   ██║██║     █████╗  ███████║██╔██╗ ██║
██╔══╝  ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██║██║╚██╗██║██║    ██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║
██║     ███████╗██║  ██║███████╗██║     ██║██║ ╚████║██║    ╚██████╔╝╚██████╗███████╗██║  ██║██║ ╚████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝     ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                       
  ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
    """)
    elif character["Level"] == 4:
        print("\nThis is it. You go to Ultimo Lake. Home of the Final Fishtasy")
        print("""
⊹࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪˖
██╗   ██╗██╗  ████████╗██╗███╗   ███╗ ██████╗     ██╗      █████╗ ██╗  ██╗███████╗
██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔═══██╗    ██║     ██╔══██╗██║ ██╔╝██╔════╝
██║   ██║██║     ██║   ██║██╔████╔██║██║   ██║    ██║     ███████║█████╔╝ █████╗  
██║   ██║██║     ██║   ██║██║╚██╔╝██║██║   ██║    ██║     ██╔══██║██╔═██╗ ██╔══╝  
╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║╚██████╔╝    ███████╗██║  ██║██║  ██╗███████╗
 ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
⊹࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪˖
        """)
