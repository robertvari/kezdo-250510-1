import os, random

# Game Loop
while True:
    os.system("cls")
    # mac/linux
    # os.system("clear")

    # Game intro
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print("I have number between 1 and 10. Can you guess it?")
    print("You have 3 tries to guess.")

    # game difficulty
    min_number = 1
    max_number = 10
    tries = 3

    # computer guess
    magic_number = str( random.randint(min_number, max_number) )

    # get player guess
    player_guess = input("Your number: ")

    # force player to try again if the guess is wrong
    while magic_number != player_guess:
        tries -=1
        if tries == 0: break
        
        os.system("cls")
        print(f"Wrong guess. You have {tries} tries left. Try again.")
        player_guess = input("Your number: ")
    
    os.system("cls")
    # game end condition
    if magic_number == player_guess:
        print("You win! :))")
    else:
        print("You lost this round")

    player_response = input("Do you want to play again? (y/n)")
    if player_response == "n":
        os.system("cls") 
        break