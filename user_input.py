def get_user_choice():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if choice in ["higher", "lower"]:
            return choice
        else:
            print("Please enter either 'higher' or 'lower'.")
