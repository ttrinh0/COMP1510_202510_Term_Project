"""
Module info
"""

import print_or_scene
import setup
import check
import user_action
from color50 import rgb, constants


def game():
    """
    Drive the game.
    """
    print_or_scene.start_up()
    rows = 5
    columns = 5
    game_parameters = setup.create_game_parameters()
    board = setup.make_board(rows, columns, game_parameters)
    character = setup.make_character()
    complete_fish_collection = setup.make_fish_collection()
    achieved_goal = False

    print_or_scene.print_area_scene(character)
    print_or_scene.area_one_scene(character)

    while check.is_alive(character) and not achieved_goal:
        print_or_scene.ascii_board(board, character)
        print_or_scene.describe_current_location(board, character)
        choice = user_action.get_user_choice()
        action = check.process_choice(choice)

        if action == "Movement":
            valid_move = check.validate_move(board, character, choice)
            if valid_move:
                user_action.move_character(character, choice)
            else:
                print(rgb(255, 175, 175) + "You can't move there! Pick another direction." + constants.RESET)

        elif action == "Interact":
            print_or_scene.print_interact()

        elif action == "Profile":
            print_or_scene.print_player_info(character)

        elif action == "Collection":
            print_or_scene.print_fish_list(character, True)

        elif action == "Fish":
            there_is_a_fish = check.check_for_fish()
            if there_is_a_fish:
                if user_action.fishing_game(character, game_parameters):
                    fish = check.check_fish_type(character, complete_fish_collection)
                    if check.check_fish_in_collection(character, fish):
                        user_action.add_fish_to_collection(character, fish)
                        check.level_up(character, complete_fish_collection)
                        check.final_conditions(character)
                achieved_goal = check.check_if_goal_attained(character)
                print_or_scene.print_fish_list(character)

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
