"""
Module of functions that either take user input or change the player's stats
"""
import time
from color50 import rgb, constants
import random


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


def fishing_game(character, game_parameters):  # Have to add character stats
    """
    Execute a fishing mini-game.

    The user inputs the specified key a randomly determined amount of times.

    :param game_parameters: a dictionary containing the game parameters
    :param character: a dictionary containing the character information
    :precondition: user input must input a key
    :precondition: character must be a dictionary
    :precondition: character must contain the keys "Stamina", "Fishing Power", "Level", and "Fish Caught", all with
                   values of integers
    :postcondition: decreases the character's stamina by one if the user loses the game
    :postcondition: does not alter character's stamina if the user wins the game
    :postcondition: increases the character's Fish Caught count if the user wins the game
    :postcondition: prints "HIT!" when the user correctly inputs a key
    :postcondition: prints a statement that the fish gets away and the character's stamina decreases if the user loses
                    the game
    :postcondition: prints "Gotcha!" if the user wins the game
    :return False: a Boolean with the value of False if character loses the mini-game
    :return True: a Boolean with the value of True if character wins the mini-game
    """
    # set up the parameters
    level = character["Level"]
    fishing_power = character["Fishing Power"]
    input_time = game_parameters["Input Time"][level]
    fish_reel_constraints = game_parameters["Fish Reel"][level]
    wait_time = random.randint(1, 4)
    fish_reel = random.randint(level, fish_reel_constraints - fishing_power)
    win_count = 0
    print(f"You cast your rod.\nInput the specified key within {input_time} seconds when prompted!")
    for _ in range(wait_time):
        time.sleep(1)
        print("...")
    time.sleep(1)
    # The gameplay
    print("\nSomething hooks!")
    for _ in range(fish_reel):
        # The keys you need to press will be from 1 to your level + 1
        key = random.randint(1, level + 1)
        start_time = time.time()
        user_input = input(f"><(((º> Input {key}!\n")
        # the time you have to press the key will decrease depending on your level
        if time.time() - start_time > input_time or user_input != str(key):
            character["Stamina"] -= 1
            print("\nThe fish breaks free and gets away...\n"
                  "Your stamina decreases by 1\n"
                  "Current stamina:", character["Stamina"])
            return False
        else:
            print("\tHIT!")
            time.sleep(random.randint(0, 3))
            win_count += 1
            continue
    if win_count == fish_reel:
        character["Fish Caught"] += 1
        print("Gotcha!")
        return True


def get_response(message, options):
    """

    :param message: a string
    :param options: a positive integer
    :return user_input: a string containing the number that represents the player's choice
    """
    response = False

    while response is False:
        user_input = input(message)
        user_options = []
        for number in range(1, options + 1):
            user_options.append(str(number))
        if user_input in user_options:
            return user_input
        else:
            print("Please enter a valid option!")