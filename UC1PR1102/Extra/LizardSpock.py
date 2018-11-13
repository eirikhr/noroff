# LizardSpock.py
# One player version
# Eirik Rynning 2015
# Note: Uavgjort fungerer ikke, må fikses!

# Modules:
import time
import random
import getpass


def selection():
    while True:
        # change to input() if you are
        # selection = input(": ")
        selection = getpass.getpass("->", stream=None) #  ------> This doesn't work in Pycharm!:(
        if selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5":
            return selection
        else:
            print("I could not recognize your input. Please try again!")
            continue


def conversion(selection):
    if selection == "1":
        return "ROCK"
    if selection == "2":
        return "SCISSOR"
    if selection == "3":
        return "LIZARD"
    if selection == "4":
        return "PAPER"
    else:
        return "SPOCK"


def selection_text():
    print("1: Selects ROCK as your rock hard tool of combat!")
    print("2: Selects SCISSORS as your cutting edge weapon for the skirmish!")
    print("3: Selects LIZARD as your Pokemon in the battle arena!")
    print("4: Selects PAPER as your environment-friendly weapon!")
    print("5: Selects SPOCK as your blood-brother in cyber-space warfare!")

# Starting game with greeting
print("Welcome to the game Rock, paper, Scissors, Lizard, Spock!")
print("\nGame rules:")
print("Scissors cuts paper. Paper covers rock. Rock crushes lizard. Lizard poisons Spock.")
print("Spock smashes scissors. Scissors decapitates lizard. Lizard eats paper. Paper disproves Spock. Spock vaporizes rock.")
print("And, as it always has, rock crushes scissors.")
print("\nGot it? Okay, let's go!\n")

score_count = [0, 0]

while True:
    print("Computer is selecting a combat tool...")
    print("Computer has selected a combat tool. Prepare to select your own tool!\n")
    player2 = random.randint(1,5)
    print("HE CHOSE ", player2)
    print("Player 1: Make a choice:")
    selection_text()
    player1 = selection()
    print("\nBoth has made their selection. The results are:")
    time.sleep(.3)
    print("Calculating...")
    time.sleep(.3)
    print("Calculating some more....")
    time.sleep(.3)
    print("Come on, this is such hard calculations!\n")
    time.sleep(1)

    winner = ((int(player1) - int(player2)) % 5)
    if winner == 3 or winner == 4:
        print("Player 1 wins after knocking out the computers", conversion(player2), "with his", conversion(player1))
        score_count[0] = score_count[0] + 1
    if player1 == player2:
        print("Its a draw! Both chose", conversion(winner), "!")
    else:
        print("The computer wins after knocking out your", conversion(player1), "with his", conversion(player2))
        score_count[1] = score_count[1] + 1

    while True:
        repeat = input("\nDo you want to play again? Type yes or no:")
        if repeat.lower() == "no" or repeat.lower() == "n":
            print("Thanks for playing!")
            print("The final score is:")
            print("Player 1:", score_count[0], "point.\nComputer:", score_count[1], "point.")
            quit()
        elif repeat.lower() == "yes" or repeat.lower() == "y":
            print("\nThe score is:")
            print("Player 1:", score_count[0], "point.\nComputer:", score_count[1], "point.\n\n")
            break
        else:
            print("\nInvalid input. Try again.")
            continue

    continue