"""
A collection of functions used to simply print scenes and information to the player.
"""
import random
import time
import setup
import user_action
import itertools
from table2ascii import table2ascii, PresetStyle
from color50 import rgb, constants


def ascii_board(board: dict, character: dict, game_parameters: dict) -> None:
    """
    Print the game board using ascii.

    :param game_parameters:
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
    rows = max(board)[0] + 1
    columns = max(board)[1] + 1
    for number in range(rows):
        board_rows.append(board_spaces.copy())
        for element in range(columns):
            board_rows[number].append("  ")

    if character["Level"] == 1:
        for coordinate in game_parameters["Level Map"]["Event Coordinates One"]:
            board_rows[coordinate[1]][coordinate[0]] = "⏅"
    if character["Level"] == 2:
        for coordinate in game_parameters["Level Map"]["Event Coordinates Two"]:
            board_rows[coordinate[1]][coordinate[0]] = "⏅"
    if character["Level"] == 3:
        for coordinate in game_parameters["Level Map"]["Event Coordinates Three"]:
            board_rows[coordinate[1]][coordinate[0]] = "⏅"
    if character["Level"] == 4:
        for coordinate in game_parameters["Level Map"]["Event Coordinates Final"]:
            board_rows[coordinate[1]][coordinate[0]] = "✦"

    board_rows[character["Y-coordinate"]][character["X-coordinate"]] = "⛵"
    output = table2ascii(
        body=board_rows,
        style=PresetStyle.ascii_box
    )
    print(output)


def describe_current_location(board: dict, character: dict) -> None:
    """
    Print the character's current coordinates and the game board.

    :param board: a dictionary containing the game board coordinates
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: board must contain keys containing the game board coordinates
    :precondition: character must be a dictionary
    :precondition: character must contain keys-value pairs of the coordinates
    :postcondition: prints the character's current coordinates and the ascii game board
    """
    current_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    location_description = board[current_coordinates]
    if location_description[0] == "Fisher":
        message = (rgb(240, 230, 150) + "You are currently at " +
                   str(current_coordinates) + ". There's a fisher nearby." + constants.RESET)
    elif location_description[0] == "Coin":
        message = (rgb(240, 230, 150) + "You are currently at " +
                   str(current_coordinates) + ". There's something on that rock." + constants.RESET)
    else:
        message = rgb(240, 230, 150) + "You are currently at " + str(current_coordinates) + "." + constants.RESET
    print(message)


def print_fish_list(character: dict, collection: bool = False) -> None:
    """
    Print out the player's current fish collection.

    The fish the player has not caught will be printed as ???.

    :param character: a dictionary containing the character information
    :param collection: a Boolean of True or False
    :precondition: character has the key "Fish Collection"
    :precondition: collection will be set to False by default unless specified as True
    :precondition: if collection is set to False, will ask the user to press enter to continue
    :postcondition: prints a numbered collection of fish, showing which fish the player has caught
    :postcondition: fish the player has not caught will be labeled as ???
    :postcondition: if collection is set to True, will run the cycle_fish function
    """

    def cycle_fish():
        """
        Allow the player to select a fish to view its name and description and cycle through their collection.

        :precondition:
        :return:
        """
        fish_list_values = [viewed_fish for viewed_fish in character["Fish Collection"].values()]
        fish_generator = itertools.cycle(fish_list_values)
        user_message = rgb(0, 255, 255) + "Enter the number of a fish to view or q to go back.\n" + constants.RESET
        fish_start = user_action.get_response(user_message, 11, True)
        if fish_start == "q":
            return False
        fish_generator = itertools.islice(fish_generator, int(fish_start) - 1, None)
        user_input = False
        while not user_input:
            name = next(fish_generator)
            if name == ('???', '???'):
                name = ("???", "You have not unlocked this fish yet!")
            print(rgb(255, 255, 255) + name[0] + constants.RESET + ": " + name[1])
            user_input = input(rgb(0, 255, 255) + "press d to view the next fish, q to quit\n" + constants.RESET)
            if user_input == "q":
                user_input = True
            elif user_input == "d":
                user_input = False
            else:
                print(rgb(255, 175, 175) + "Please enter a valid option!" + constants.RESET)
                user_input = False

    fish_list = sorted(character["Fish Collection"].items())
    print("\tFish Collection")
    print("-" * 23)
    for number, fish in enumerate(fish_list, 1):
        print(f"{number}: {fish[1][0]}")
    print("-" * 23)
    if not collection:
        input(rgb(125, 170, 190) + "♦ Press enter to continue ♦" + constants.RESET)
    else:
        cycle_fish()


def print_player_info(character: dict):
    """
    Print the player's information.

    :param character: a dictionary containing the character information
    :precondition: character has the keys "Name", "Title", "Level", "Stamina", "Max Stamina", "Fishing Power",
                   and "Fish Caught"
    :postcondition: prints out the player's information
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
    input(rgb(125, 170, 190) + "♦ Press enter to continue ♦" + constants.RESET)


def area_one_scene(character: dict) -> None:
    """
    Prints out the scene when the player enters the first area.

    :param character: a dictionary containing the character information
    :precondition: character has the keys "Name", "Stamina", "Max Stamina", and "Fishing Power"
    :postcondition: prints out the scene when the player enters the first area
    """
    print(rgb(240, 230, 150) + '"Hey!"')
    time.sleep(1)
    print('"You!"\n' + constants.RESET)
    input(rgb(125, 170, 190) + "♦ Press enter to continue ♦" + constants.RESET)
    print(
        "\nYou look around and a man fully decked out in fish gear catches your eye. You are amazed at just how many \n"
        "fish related accessories he has attached to his belt.\n")
    input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
    print("\nHe enthusiastically waves at you as he drives his boat next to yours.")
    time.sleep(1)
    print(rgb(240, 230, 150) + '\n"Bahahaha! You\'re new here, aren\'tcha."')
    print('"What\'s your name, newbie?"\n' + constants.RESET)
    setup.get_name(character)
    name = character["Name"]
    print(rgb(240, 230, 150) + f'\n"{name}? That\'s a fine name! They call me Marlin."')
    time.sleep(1)
    print('\n"Is that a new fishing rod? It\'s got that new rod smell."')
    time.sleep(1)
    print('"Hey! I know that that brand, which version did you get?"\n' + constants.RESET)
    time.sleep(1)
    rod = setup.choose_rod(character)
    print(rgb(240, 230, 150) + f"\nThe {rod}, eh?")
    if rod == "Stamina Rod":
        print('"Good choice! That rod is light and easy on the body. Might not be as powerful but you\'ll be able to '
              'fish for longer.' + constants.RESET + '\n[Stamina: 6, Fishing Power: 4]\n')
    elif rod == "Power Rod":
        print('"Good choice! That rod is quite powerful. It\'s a little heavy, but I\'d say catching fish will be a bit'
              ' easier."' + constants.RESET + '\n[Stamina: 4, Fishing Power: 6]\n')
    time.sleep(1)
    print(rgb(240, 230, 150) + f'"So, {name}, you need some pointers on how to fish?"\n' + constants.RESET)
    message_fish = rgb(0, 255, 255) + """Do you want to hear the tutorial?:
    1 - Yes please!
    2 - No thanks! I can figure it out!
""" + constants.RESET
    answer_fish = user_action.get_response(message_fish, 2)
    if answer_fish == "1":
        print(rgb(240, 230, 150) + '\n"Bahahaha! Don\'t fret, little guppy, I\'ll show you the ropes."'
              + constants.RESET)
        print_fishing_demo()
    elif answer_fish == "2":
        print(rgb(240, 230, 150) + '"Well, don\'t let me hold you up then. Best of luck,', name + '!"'
              + constants.RESET)


def print_fishing_demo() -> None:
    """
    Print a tutorial for the fishing minigame.

    :precondition: player has selected to see the tutorial demo
    :postcondition: prints the tutorial for the minigame
    """
    repeat = False
    while not repeat:
        time.sleep(1)
        print(rgb(240, 230, 150) + '"Listen here and pay attention, my friend"\n' + constants.RESET)
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
        print('He takes his fishing rod and gracefully casts it into the lake.')
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Something hooks!\n")
        time.sleep(1)
        print(rgb(240, 230, 150) + '"This is where the challenge really begins!"\n')
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
        print(rgb(240, 230, 150) + '"You\'ll feel a tug, each time you feel it. You\'re gonna wanna reel'
                                   ' and pull it back!"' + constants.RESET)
        print("[A message will pop up, prompting you to input a key.]")
        time.sleep(1)
        print('[><(((º> Input 2!]\n')
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
        print('[When you see this message, input the number you see. In this case, enter 2.]\n')
        print(rgb(240, 230, 150) + '"And don\'t let your mind wander! If you\'re too slow, '
                                   'the fish will get away!"' + constants.RESET)
        print('[If you\'re successful, you\'ll get a "HIT!" message]\n')
        time.sleep(1)
        print(rgb(255, 255, 0) + "\tHIT!\n" + constants.RESET)
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
        print(rgb(240, 230, 150) + '"You\'ll have to do this a couple times before you\'re able to catch the fish."\n')
        print('"I think that\'s about all from me. Do you need me to go over it again?"\n' + constants.RESET)
        repeat_message = rgb(0, 255, 255) + """Would you like to see the tutorial again?:
    1 - Yes, I need to hear it again!
    2 - No, I got it!
    """ + constants.RESET
        repeat = user_action.get_response(repeat_message, 2)
        if repeat == "1":
            print(rgb(240, 230, 150) + '\n"You need to hear it again? Alrighty."' + constants.RESET)
            repeat = False
        elif repeat == "2":
            print("\nHe nods.\n")
            print(rgb(240, 230, 150) + '"You\'ll run into some more challenging fish as you go on your '
                                       'fisher journey.\nBet you\'re also looking to catch the Final Fishasy, eh?')
            print('Best of luck, my friend!"\n' + constants.RESET)
            input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
            print("\n\n࿔･ﾟ﹏𓊝﹏༄.°\n\n")
            repeat = True


def print_interact(character: dict, game_parameters: dict) -> None:
    """
    Print a message to the player.

    If the player is on certain coordinates, specific messages will print, else a random message will print.

    :param character: a dictionary containing the character information
    :param game_parameters: a dictionary containing the game parameters
    :precondition: character contains "X-coordinate", "Y-coordinate", and "Level"
    :precondition: game_parameters contains "Level Map" and its dictionary value dictionaries of level maps
    :postcondition: prints a message that is randomly chosen if player is on a regular coordinate
    :postcondition: prints a specific message if the player is on a specific coordinate
    """

    coordinate = (character["X-coordinate"], character["Y-coordinate"])
    level_maps = [level_map for level_map in game_parameters["Level Map"]]
    level = character["Level"] - 1
    current_map = level_maps[level]
    if coordinate not in game_parameters["Level Map"][current_map]:
        regular_message_bank = {"The breeze is nice.",
                                "You see other fishers fishing",
                                "It's such a nice day today.",
                                "You look into the water below you. It looks back are you"}
        message = random.choice(list(regular_message_bank))
        print(message)

    elif coordinate in game_parameters["Level Map"][current_map]:
        npc_type = game_parameters["Level Map"][current_map][coordinate][0]
        if npc_type == "Fisher":
            print("You wave to the nearby fisher.")
        fisher_npc = game_parameters["Level Map"][current_map][coordinate][1]
        print_fisher_npc(character, fisher_npc)
    input(rgb(125, 170, 190) + "♦ Press enter to continue ♦" + constants.RESET)


def print_fisher_npc(character: dict, fisher_npc: str) -> None:
    """
    Print a specific message depending on which NPC is talked to.

    :param character: a dictionary containing the character information
    :param fisher_npc: a string containing the name of the npc/object
    :precondition: character contains the keys "NPC Talk", "Stamina", "Max Stamina", and "Fishing Power"
    :postcondition: player's "Stamina", "Max Stamina", and/or "Fishing Power" increases depending on fisher_npc
    :postcondition: prints a message to the player
    """
    npc_has_talked = character["NPC Talk"][fisher_npc]

    if fisher_npc == "Sally" and not npc_has_talked:
        print("The fisher waves back.")
        print(rgb(240, 230, 150) + '"An unfamiliar face! How exciting. I\'m Sally. I love fishing, it\'s relaxing.\n'
                                   'I really hope you enjoy your time here at Initium Pond!"\n' + constants.RESET)
        print("The nice conversation left you in a good mood.")
        print(rgb(0, 255, 0) + "[Max Stamina +1!]" + constants.RESET)
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Sally" and npc_has_talked:
        print("Sally: ", end="")
        print(rgb(240, 230, 150) + '"Enjoy your time here, fisher!"' + constants.RESET)

    if fisher_npc == "Charles" and not npc_has_talked:
        print("The fisher lifts his head when he notices you. He waves sleepily.")
        print(rgb(240, 230, 150) + '"Mhmhh, good day, fisher. Name\'s Charles. I swear I\'m not falling asleep, '
                                   'it\'s just that no fish are biting right now...\n'
                                   'Maybe I\'m scaring them away, staying in the same spot for so long..."'
              + constants.RESET)
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Charles" and npc_has_talked:
        print("Sally: ", end="")
        print("You hear Charles speaking under his breath.")
        print(rgb(240, 230, 150) + '"...Maybe I should move to another spot... but I\'m tired..."' + constants.RESET)

    if fisher_npc == "Rob" and not npc_has_talked:
        print("A fisher is focused on his cast.")
        print(rgb(240, 230, 150) + '"Aw man!"' + constants.RESET)
        print("The fisher sadly reels his line to reveal an empty hook\n"
              "He finally notices you.")
        print(rgb(240, 230, 150) + '"Oh, hello! I\'m Rob... You didn\'t see that did you?\n'
                                   'Well... um. Here take this."' + constants.RESET)
        print("Rob throws you a very sparkly fish charm.")
        print(rgb(240, 230, 150) + '"I think they\'re awesome."' + constants.RESET)
        print(rgb(0, 255, 0) + "[Fishing Power +1!]" + constants.RESET)
        character["Fishing Power"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Rob" and npc_has_talked:
        print(rgb(240, 230, 150) + '"This one\'s the one..."' + constants.RESET)

    if fisher_npc == "Cornet" and not npc_has_talked:
        print("The fisher waves back enthusiastically. They seem to be doing great with their catches")
        print(rgb(240, 230, 150) + '"Hiiiiiii! I\'m Cornet! Here, take this, hope it helps!"'
              + constants.RESET)
        print("Cornet throws a cool fish hook to you.")
        print(rgb(0, 255, 0) + "[Fishing Power +1!]" + constants.RESET)
        character["Fishing Power"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Cornet" and npc_has_talked:
        print(rgb(240, 230, 150) + "You hear them humming a tune as they wait for a "
                                   "fish to bite." + constants.RESET)

    if fisher_npc == "Gilly" and not npc_has_talked:
        print("The fisher also waves.\nShe doesn't say much, but she points at the name written on her boat, \"Gilly\","
              " and then points to herself.\nYou take that to mean her name is Gilly. You stay beside her for a "
              "while.\nIt's calming.")
        print(rgb(0, 255, 0) + "[Stamina +1!]" + constants.RESET)
        if character["Stamina"] < character["Max Stamina"]:
            character["Stamina"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Gilly" and npc_has_talked:
        print("Gilly smiles at you.")

    if fisher_npc == "Sandy" and not npc_has_talked:
        print(rgb(240, 230, 150) + '"Hi there, friend. I\'m selling cool rocks. Limited time rocks. \n'
                                   'Would you like to support me? No? We\'re at a river with tons of rocks?\n Well what'
                                   ' if I throw in this bottle of water? Still no? '
                                   'Darn. Well have this water bottle anyways, stay hydrated."')
        print(rgb(0, 255, 0) + "[Stamina +1!]" + constants.RESET)
        if character["Stamina"] < character["Max Stamina"]:
            character["Stamina"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Sandy" and npc_has_talked:
        print(rgb(240, 230, 150) + '"Man... no one wants my rocks"' + constants.RESET)

    if fisher_npc == "Emile" and not npc_has_talked:
        print("The fisher doesn't notice you, but the other man in the boat does. He waves politely.")
        print(rgb(240, 230, 150) + '"Good day, fisher. Don\'t mind him, he\'s a bit shy. I\'m Emile, '
                                   'the lovely man fishing is Rori.\nOh! You\'re trying to find the Final Fishasy?'
                                   'I wish you the best of luck!"' + constants.RESET)
        print("The nice conversation left you in a good mood.")
        print(rgb(0, 255, 255) + "[Stamina +1!]" + constants.RESET)
        if character["Stamina"] < character["Max Stamina"]:
            character["Stamina"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Emile" and npc_has_talked:
        print("You see Emile laughing with Rori.")

    if fisher_npc == "Aqua" and not npc_has_talked:
        print("The fisher smiles big.")
        print(rgb(240, 230, 150) + '"Hehehe, I see your equipment. I see the fish. Final Fishasy right?'
                                   'I\'m Aqua by the way.\nSeems like quite the challenge! Well, I\'ll let you '
                                   'get on your way. But, here."' + constants.RESET)
        print("She throws a granola bar your way.")
        print(rgb(240, 230, 150) + '"Keep your strength up, right?"' + constants.RESET)
        print(rgb(0, 255, 255) + "[Stamina +1!]" + constants.RESET)
        if character["Stamina"] < character["Max Stamina"]:
            character["Stamina"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Aqua" and npc_has_talked:
        print("Aqua nods at you.")

    if fisher_npc == "Coin" and not npc_has_talked:
        print(
            "You see a shiny coin on a rock. It's too far to reach, but you admire it from afar.\n"
            "It must be a sign of good luck. You'll need it to catch the Final Fishasy.\n")
        print(rgb(0, 255, 0) + "[Stamina +1!]\n[Fishing Power +1!]" + constants.RESET)
        if character["Stamina"] < character["Max Stamina"]:
            character["Stamina"] += 1
        character["Fishing Power"] += 1
        character["NPC Talk"][fisher_npc] = True
    elif fisher_npc == "Coin" and npc_has_talked:
        print("The coin shines.")


def start_up():
    """
    Print a start-up screen.

    :precondition: player runs the program
    :postcondition: prints a start-up screen to the player
    """
    print(r"""
███████╗██╗███╗   ██╗ █████╗ ██╗                             
██╔════╝██║████╗  ██║██╔══██╗██║                             
█████╗  ██║██╔██╗ ██║███████║██║                             
██╔══╝  ██║██║╚██╗██║██╔══██║██║                             
██║     ██║██║ ╚████║██║  ██║███████╗                        
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                        
███████╗██╗███████╗██╗  ██╗ █████╗ ███████╗██╗   ██╗      /`·.¸
██╔════╝██║██╔════╝██║  ██║██╔══██╗██╔════╝╚██╗ ██╔╝     /¸...¸`:·  
█████╗  ██║███████╗███████║███████║███████╗ ╚████╔╝   ¸.·´  ¸   `·.¸.·´)  
██╔══╝  ██║╚════██║██╔══██║██╔══██║╚════██║  ╚██╔╝   : © ):´;      ¸  {   
██║     ██║███████║██║  ██║██║  ██║███████║   ██║     `·.¸ `·  ¸.·´\`·¸)
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝         `\\´´\¸.·´
Final Fishasy
""")
    input(rgb(255, 255, 255) + "♦ Press enter to continue ♦" + constants.RESET)
    print("Today is the day.\n"
          "T"
          "he day you're going to start your fishing journey!")
    input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
    print("Recently, a story had been popping up around town about a legendary fish called\n\n"
          "\tThe Final Fishasy"
          "\n\nAnd you're gonna be the one who will catch it!\n"
          "You gather you equipment and make your way out the door.")
    input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)


def print_area_scene(character: dict) -> None:
    """
    Print a scene of the player moving to a new area.

    :param character: a dictionary containing the character information
    :precondition: character contains the key "Level"
    :postcondition: prints a small message and then a title screen of the name of the new area
    """
    if character["Level"] == 1:
        print("\nYou make your way to Initium Pond. A calm pond full of fish.")
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
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
        print("\nYou go to the Medius River")
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
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
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
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
        print("\nThis is it. You go to Ultimo Lake. Home of the Final Fishasy")
        input(rgb(150, 195, 215) + "♦ Press enter to continue ♦" + constants.RESET)
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
    elif character["Level"] == 5:
        print("\nYou go back home in triumph.")


def print_end_scene(character: dict) -> None:
    """
    Print a celebratory ending scene for the player.

    This will print when the player wins the game.

    :param character: a dictionary containing the character information
    :precondition: character contains the keys "Name", "Fishing Power", "Stamina", "Max Stamina", "Title",
                   "Fish Collection", "NPC Talk", "Fish Caught"
    :postcondition: prints a celebratory ending scene for the player
    :postcondition: prints the player's final stats
    """
    # also shows the player's final stats
    pass