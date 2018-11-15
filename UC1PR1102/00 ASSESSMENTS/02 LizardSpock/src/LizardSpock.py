# LizardSpock.py
# Version: 2.0
# Eirik Rynning 2018

# Modules:
import time
import random
import getpass
import sys
import os


def getinput():
    """Gets value from user"""
    value = input("-> ")
    return value


def menuselection():
    """Prints main menu and resets score."""
    global score_count
    score_count = [0, 0]
    print("1: One player version.")
    print("Quit the game by entering q")
    selected = getinput()
    return selected


def selection():
    """Takes and returns selection of preffered weapon from user. """
    while True:
        # change to input() if you are using PyCharm interpreter:
        # selection = input(": ")
        selection = getpass.getpass("-> ", stream=None)
        if selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5":
            return selection
        if selection.lower() == "q" or selection.lower() == "quit":
            quit()
        else:
            print("I could not recognize your input. Please try again!")
            continue


def conversion(selection):
    """Converts numeral selection to its text value.

    Args:
        selection (str): Numerical value as string.
    """
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
    """Prints the users numeral choices for selection. """
    print("1: Selects ROCK as your rock hard tool of combat!")
    print("2: Selects SCISSORS as your cutting edge weapon for the skirmish!")
    print("3: Selects LIZARD as your Pokemon in the battle arena!")
    print("4: Selects PAPER as your environment-friendly weapon!")
    print("5: Selects SPOCK as your blood-brother in cyber-space warfare!")


def loading(count=60):
    """Prints dots to the screen without newline.

    Args:
        count (int): Amount of dots to print.
    """
    for i in range(count):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.01)
        count -= 1
    print("\n\n")


"""

# Starting game with greeting
print("Welcome to the game Rock, paper, Scissors, Lizard, Spock!")
print("\nGame rules:")
print("Scissors cuts paper. Paper covers rock. Rock crushes lizard. Lizard poisons Spock.")
print("Spock smashes scissors. Scissors decapitates lizard. Lizard eats paper. Paper disproves Spock. Spock vaporizes rock.")
print("And, as it always has, rock crushes scissors.")
print("\nGot it? Okay, let's go!\n")

"""



def onePlayer():
    while True:
        print("Computer is selecting a combat tool...")
        print("Computer has selected a combat tool. Prepare to select your own tool!\n")
        player2 = str(random.randint(1, 5))
        loading()
        print("COMPUTER CHOSE ", player2)  # For testing purposes.
        print("Player 1: Make a choice:")
        selection_text()
        player1 = selection()
        print("\nBoth has made their selection. The results are:")
        time.sleep(.03)
        print("\nCalculating...")
        loading()
        winner = ((int(player1) - int(player2)) % 5)
        if player1 == player2:
            print("Its a draw! Both chose", conversion(str(winner)), "!")
        if winner == 3 or winner == 4:
            print("Player 1 wins after knocking out the computers", conversion(player2), "with his", conversion(player1))
            score_count[0] = score_count[0] + 1
        else:
            print("The computer wins after knocking out your", conversion(player1), "with his", conversion(player2))
            score_count[1] = score_count[1] + 1
        repeat = input("\nDo you want to play again? Type yes or no: \n-> ")
        if repeat.lower() == "no" or repeat.lower() == "n":
            print("Thanks for playing!")
            print("The final score is:")
            print("Player 1:", score_count[0], "point.\nComputer:", score_count[1], "point.")
            break
        elif repeat.lower() == "yes" or repeat.lower() == "y":
            print("\nThe score is:")
            print("Player 1:", score_count[0], "point.\nComputer:", score_count[1], "point.\n\n")
            continue
        else:
            print("\nInvalid input. Try again.")
            continue


# Variables
score_count = [0, 0]
os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for readability


while True:

    maininput = menuselection()
    if maininput == "1":
        loading(30)
        onePlayer()
    if maininput.lower() == "q":
        quit()
    else:
        print("Invalid entry. Try again.")
        continue
