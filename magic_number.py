# Game Loop
while True:
    # Game intro
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print("I have number between 1 and 10. Can you guess it?")
    print("You have 3 tries to guess.")

    # game difficulty
    min_number = 1
    max_number = 10
    tries = 3

    # computer guess
    magic_number = 5

    # get player guess

    player_response = input("Do you want to play again? (y/n)")
    if player_response == "n": break