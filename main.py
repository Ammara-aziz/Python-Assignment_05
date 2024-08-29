from game_logic import generate_numbers, check_guess
from user_input import get_user_choice
from constants import NUM_ROUNDS

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        
        player_number, computer_number = generate_numbers()
        print(f"Your number is {player_number}")
        
        choice = get_user_choice()
        
        if check_guess(player_number, computer_number, choice):
            score += 1
            print(f"You were right! The computer's number was {computer_number}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  # Blank line for separating rounds

    print("Thanks for playing!")
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
