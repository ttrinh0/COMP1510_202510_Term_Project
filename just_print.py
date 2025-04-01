"""
A collection of functions used to simply print scenes and information to the player.
"""


def print_fish_collection(character):
    """
    Print the player's fish collection.
    :param character:
    """
    fish_list = sorted(character["Fish Collection"].values())
    print("\tFish Collection")
    print("-" * 23)
    for number, fish in enumerate(fish_list, 1):
        print(f"{number}: {fish[0]}")
    print("-" * 23)


def print_player_info(character):
    """
    Print the player's information.
    :param character:
    """
    print("\tPlayer Information")
    print("-" * 26)
    print("Name: " + character["Name"] +
          "\nTitle: " + str(character["Level"][1]) +
          "\nLevel: " + str(character["Level"][0]) +
          "\nStamina: " + str(character["Stamina"]) +
          "\nFishing Power: " + str(character["Fishing Power"]) +
          "\nFish Caught: " + str(character["Fish Caught"]))
    print("-" * 26)
