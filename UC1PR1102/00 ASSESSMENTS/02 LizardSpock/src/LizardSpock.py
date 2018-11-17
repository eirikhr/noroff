# LizardSpock.py
# Version: 2.0
# Eirik Rynning 2018

# Modules:
import time
import sys
import os
from getpass import getpass
from random import randint
import testing2



def itssimple():
    """Returns why the winner won the round."""
    if player1 == "1" and player2 == "2":
        print("ROCK crushes SCISSORS.")
    if player1 == "1" and player2 == "3":
        print("ROCK crushes LIZARD.")
    if player1 == "1" and player2 == "4":
        print("PAPER covers ROCK.")
    if player1 == "1" and player2 == "5":
        print("SPOCK vaporizes ROCK.")
    if player1 == "2" and player2 == "1":
        print("ROCK crushes SCISSORS.")
    if player1 == "2" and player2 == "3":
        print("SCISSORS decapitates LIZARD.")
    if player1 == "2" and player2 == "4":
        print("SCISSORS cuts PAPER.")
    if player1 == "2" and player2 == "5":
        print("SPOCK smashes SCISSORS.")
    if player1 == "3" and player2 == "1":
        print("ROCK crushes LIZARD.")
    if player1 == "3" and player2 == "2":
        print("SCISSORS decapitates LIZARD.")
    if player1 == "3" and player2 == "4":
        print("LIZARD eats PAPER.")
    if player1 == "3" and player2 == "5":
        print("LIZARD poisons SPOCK")
    if player1 == "4" and player2 == "1":
        print("PAPER covers ROCK.")
    if player1 == "4" and player2 == "2":
        print("SCISSORS cuts PAPER.")
    if player1 == "4" and player2 == "3":
        print("LIZARD eats PAPER.")
    if player1 == "4" and player2 == "5":
        print("PAPER disproves SPOCK.")
    if player1 == "5" and player2 == "1":
        print("SPOCK vaporizes ROCK.")
    if player1 == "5" and player2 == "2":
        print("SPOCK smashes SCISSORS.")
    if player1 == "5" and player2 == "3":
        print("LIZARD poisons SPOCK")
    if player1 == "5" and player2 == "4":
        print("PAPER disproves SPOCK.")


def getinput(printstring=""):
    """Returns value from user

    Args
        printstring (str): Outputs printstring to screen before returning input from user

    """
    printstring = str(printstring)
    if len(printstring) > 0:
        print(printstring)
    value = input("-> ")
    if value.lower() == "q" or value.lower() == "quit":
        print("Thanks for playing :)")
        quit()
    return value


def gethiddeninput(printstring=""):
    """Returns value from user. User input will be hidden in console because method used are getpass() from
    the getpass module. Purpose is to hide input when being more then one player.

    Args
        printstring (str): If given, outputs 'printstring' to screen before receiving input from user

    """
    printstring = str(printstring)
    if len(printstring) > 0:
        print(printstring)
    value = getpass("-> ", stream=None)
    if value.lower() == "q" or value.lower() == "quit":
        print("Thanks for playing :)")
        quit()
    return value


def menuselection():
    """Clears screen, prints main menu and resets score. Also prints score of last round if any player scored points."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for readability
    global score_count
    if int(snakescore) > 0:
        print("You managed to score: {} points in snake!".format(snakescore))
    if score_count[0] > 0 or score_count[1] > 0:
        print("THE FINAL SCORE WAS:")
        thescoreis()
    score_count = [0, 0]
    print("--- MAIN MENU ---")
    print("1: One player version.")
    print("2: Two player version.")
    print("3: blah blah")
    print("Quit the game by entering q")
    selected = getinput()
    return selected


def selection():
    """Takes and returns selection of preffered weapon from user. """
    while True:
        # change to input() if you are using PyCharm interpreter:
        # selection = input(": ")
        selection = gethiddeninput()
        if selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5":
            return selection
        if selection.lower() == "q" or selection.lower() == "quit":
            quit()
        else:
            print("I could not recognize your input. Please try again!")
            continue


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
        time.sleep(.005)
        count -= 1
    print("\n\n")


def thescoreis():
    print()
    print(p1 + ":", score_count[0])
    print(p2 + ":", score_count[1])
    print()


def oneplayer():
    while True:
        while True:
            global player1, player2
            os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for readability
            loading(10)
            print("Computer has selected a combat tool. Prepare to select your own tool!\n")
            player2 = str(randint(1, 5))
            loading()
            print("COMPUTER CHOSE ", player2)  # For testing purposes.
            print(p1 + ": Make a choice!")
            selection_text()
            player1 = selection()
            print("\nBoth has made their selection. The results are:")
            time.sleep(.03)
            print("\nCalculating...")
            loading()
            winner = ((int(player1) - int(player2)) % 5)
            if winner == 3 or winner == 4:
                itssimple()
                print(p1, "WINS over", p2 + "!!!")
                score_count[0] = score_count[0] + 1
                break
            elif player1 == player2:
                print("This round was a DRAW!")
                break
            else:
                itssimple()
                print(p2, "WINS over", p1 + "!!!111")
                score_count[1] = score_count[1] + 1
                break
        print("POINT OVERVIEW:")
        thescoreis()
        repeat = getinput("Want to play again?\nEnter no (n) to return to the main menu.\n"
                          "Press anything else to continue.")
        if repeat.lower() == "no" or repeat.lower() == "n":
            break
        else:
            continue


# Standard Variables
score_count = [0, 0]
snakescore = 0
p1 = "Player 1"
p2 = "Computer"

while True:
    maininput = menuselection()
    if maininput == "1":
        p1 = getinput("Please enter Player 1's name:")
        loading(30)
        p2 = "Computer"
        oneplayer()
    if maininput == "2":
        p1 = getinput("Please enter Player 1's name:")
        p2 = getinput("Please enter Player 2's name:")
        loading(30)
        twoplayer()
    if maininput == "3":
        snakescore = testing2.startgame()
        continue
    if maininput.lower() == "q":
        print("Thanks for playing!")
        quit()
    else:
        continue
