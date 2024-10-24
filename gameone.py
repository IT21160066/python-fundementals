import random


def get_choices():
    first_player_choice = input("Enter first player choice: ")
    options = ["rock", "paper", "scissor"]
    second_player_option = random.choice(options)
    second_player_choice = second_player_option
    choice = {"player_one": first_player_choice, "player_two": second_player_choice}

    return choice


def check_winner(first_player, second_player):
    print("First player chose :" + first_player)
    print(f"Second player chose : {second_player}")
    if first_player == second_player:
        return "It's a tie!"
    elif first_player == "rock":
        if second_player == "scissor":
            return "First player win with rock!"
        else:
            return "Second player win with paper!"
    elif first_player == "scissor":
        if second_player == "paper":
            return "First player win with scissor!"
        else:
            return "Second player win with rock!"
    elif first_player == "paper":
        if second_player == "rock":
            return "First player win with paper!"
        else:
            return "Second player win with scissor!"
    else:
        return "Something went wrong!"


choices = get_choices()
result = check_winner(choices["player_one"], choices["player_two"])
print(result)