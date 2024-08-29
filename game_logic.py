import random

def generate_numbers():
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    return player_number, computer_number

def check_guess(player_number, computer_number, choice):
    if player_number == computer_number:
        return False  # The computer wins in case of a tie
    elif (player_number > computer_number and choice == "higher") or (player_number < computer_number and choice == "lower"):
        return True
    else:
        return False
