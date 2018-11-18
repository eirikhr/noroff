"""
LizardSpock.py
Version: 2.0
Eirik Rynning 2018
"""

# Modules:
import time
import sys
import os

from getpass import getpass
from random import randint
from bonus import main as bonusgame


def clear_screen():
    """Clears screen for readability."""
    # If client runs Windows (NT), uses "cls", else uses "clear".
    os.system("cls" if os.name == "nt" else "clear")


def its_simple(r1, r2):
    """Returns why the winner won, if it wasn't clear already.
    Because it's simple.
    According to Sheldon Cooper...

    Args:
        r1 (str): Choice of player one.
        r2 (str): Choice of player two.

    Returns:
        Why the winner won the round. For example:
        "PAPER disproves SPOCK"
    """
    if r1 == "1" and r2 == "2":
        return "ROCK crushes SCISSORS."
    if r1 == "1" and r2 == "3":
        return "ROCK crushes LIZARD."
    if r1 == "1" and r2 == "4":
        return "PAPER covers ROCK."
    if r1 == "1" and r2 == "5":
        return "SPOCK vaporizes ROCK."
    if r1 == "2" and r2 == "1":
        return "ROCK crushes SCISSORS."
    if r1 == "2" and r2 == "3":
        return "SCISSORS decapitates LIZARD."
    if r1 == "2" and r2 == "4":
        return "SCISSORS cuts PAPER."
    if r1 == "2" and r2 == "5":
        return "SPOCK smashes SCISSORS."
    if r1 == "3" and r2 == "1":
        return "ROCK crushes LIZARD."
    if r1 == "3" and r2 == "2":
        return "SCISSORS decapitates LIZARD."
    if r1 == "3" and r2 == "4":
        return "LIZARD eats PAPER."
    if r1 == "3" and r2 == "5":
        return "LIZARD poisons SPOCK"
    if r1 == "4" and r2 == "1":
        return "PAPER covers ROCK."
    if r1 == "4" and r2 == "2":
        return "SCISSORS cuts PAPER."
    if r1 == "4" and r2 == "3":
        return "LIZARD eats PAPER."
    if r1 == "4" and r2 == "5":
        return "PAPER disproves SPOCK."
    if r1 == "5" and r2 == "1":
        return "SPOCK vaporizes ROCK."
    if r1 == "5" and r2 == "2":
        return "SPOCK smashes SCISSORS."
    if r1 == "5" and r2 == "3":
        return "LIZARD poisons SPOCK"
    if r1 == "5" and r2 == "4":
        return "PAPER disproves SPOCK."


def getinput(printstring=""):
    """Outputs the argument to screen, and returns the user input.

    Args
        printstring (str): Outputs printstring to screen before returning input from user

    Returns:
        The user input.
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
    """Outputs the argument to screen, and takes a hidden user input using getpass.

    Args:
        printstring (str): If given, outputs 'printstring' to screen before receiving input from user

    Returns:
        The user input.
    """
    printstring = str(printstring)
    if len(printstring) > 0:
        print(printstring)
    value = getpass("-> ", stream=None)
    if value.lower() == "q" or value.lower() == "quit":
        print("Thanks for playing :)")
        quit()
    return value


def user_guide():
    """Sends the User Guide to the user."""
    clear_screen()
    print("------ USER GUIDE ------\n")
    print("To be completed....")
    getinput("Press anything to continue...")


def selection():
    """Ask user for selection, checks if its valid before returning the result.

    Returns:
        The users selection as a str.
    """
    while True:
        value = gethiddeninput("\nPlease select your combat tool.")
        if value == "1" or value == "2" or value == "3" or value == "4" or value == "5":
            return value
        else:
            print("I could not recognize your input.\n"
                  "Remember that your input is hidden, just like when you're typing in a password!\n"
                  "Please try again! Input one number, and press enter :)")
            continue


def conversion(value):
    """Converts numeral selection to its text value.

     Args:
        value (str): Numerical value of players choice.

    Returns:
        Translated numerical string to its text value.
    """
    if value == "1":
        return "ROCK"
    if value == "2":
        return "SCISSOR"
    if value == "3":
        return "LIZARD"
    if value == "4":
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
        time.sleep(.006)
        count -= 1
    print("\n")


def the_score_is(name1, name2, score1, score2):
    """Prints current score. To avoid repeating newlines and formatting of text.

    Args:
        name1 (str): Name of player 1.
        name2 (str): Name of player 2.
        score1 (int): Score of player 1.
        score2 (int): Score of player 2.
    """
    print()
    print(name1 + ":", score1)
    print(name2 + ":", score2)
    print()


def one_player(p1, p2):
    """Starts a new single player game.

    Args:
        p1 (str): Player 1's name.
        p2 (str): PLayer 2's name.
    """
    while True:
        while True:
            clear_screen()
            loading(30)
            player2 = str(randint(1, 5))
            print("Computer has selected a combat tool. Prepare to select your own tool!\n")
            print(p1.upper() + "!\nIts your turn to make a choice!\n")
            selection_text()
            player1 = selection()
            clear_screen()
            print("\nBoth has made their selection. The results are:")
            loading()
            winner = ((int(player1) - int(player2)) % 5)
            if winner == 3 or winner == 4:
                print(its_simple(player1, player2))
                print()
                print(p1.upper(), "IS THE WINNER!\n")
                score_count[0] = score_count[0] + 1
                break
            elif player1 == player2:
                print("\nThis round was a DRAW!")
                print("Both of you chose", conversion(player1) + "\n")
                break
            else:
                print(its_simple(player1, player2))
                print()
                print(p2.upper(), "IS THE WINNER!\n")
                score_count[1] = score_count[1] + 1
                break
        print("POINT OVERVIEW:")
        the_score_is(p1, p2, score_count[0], score_count[1])
        repeat = getinput("Want to play again?\n\nEnter no (n) to return to the main menu.\n"
                          "Press anything else to continue.")
        if repeat.lower() == "no" or repeat.lower() == "n":
            break
        else:
            continue


def two_player(p1, p2):
    """Starts a new two player game.

    Args:
        p1 (str): Player 1's name.
        p2 (str): PLayer 2's name.
    """
    while True:
        while True:
            clear_screen()
            loading(10)
            print(p1.upper() + "!\nIts your turn to make a choice!\n")
            selection_text()
            player1 = selection()
            clear_screen()
            loading(10)
            print(p2.upper() + "!\nIts your turn to make a choice!\n")
            selection_text()
            player2 = selection()
            clear_screen()
            print("\nBoth has made their selection. The results are:")
            loading()
            winner = ((int(player1) - int(player2)) % 5)
            if winner == 3 or winner == 4:
                print(its_simple(player1, player2))
                print()
                print(p1.upper(), "IS THE WINNER!\n")
                score_count[0] = score_count[0] + 1
                break
            elif player1 == player2:
                print("\nThis round was a DRAW!")
                print("Both of you chose", conversion(player1) + "\n")
                break
            else:
                print(its_simple(player1, player2))
                print()
                print(p2.upper(), "IS THE WINNER!\n")
                score_count[1] = score_count[1] + 1
                break
        print("POINT OVERVIEW:")
        the_score_is(p1, p2, score_count[0], score_count[1])
        repeat = getinput("Want to play again?\n\nEnter no (n) to return to the main menu.\n"
                          "Press anything else to continue.")
        if repeat.lower() == "no" or repeat.lower() == "n":
            break
        else:
            clear_screen()
            continue


# Declaring Global Variables
score_count = [0, 0]

# Clearing screen before init
clear_screen()


def main():
    """Main loop of this program."""
    while True:
        global score_count  # We need to access the global score.

        # Declaring some variables
        score_count = [0, 0]
        snake_score = 0
        p1 = ""
        p2 = ""

        # Printing Main Menu
        print("------ MAIN MENU ------\n")
        print("1: New Single Player Game.")
        print("2: New Two Player Game.")
        print("3: Bonus Feature.                       ------@ x")
        print("4: User Guide.")
        print("5: Exit the game.")
        print("\nNote: Quit the game completely at any time by pressing the \"q\" button\n")

        # Gets user input.
        maininput = getinput("Please enter your selection.")

        # Decide where to send user.
        if maininput == "1":
            p1 = getinput("Please enter Player 1's name:")
            loading(30)
            p2 = "Computer"
            one_player(p1, p2)
        if maininput == "2":
            p1 = getinput("Please enter Player 1's name:")
            p2 = getinput("Please enter Player 2's name:")
            loading(30)
            two_player(p1, p2)
        if maininput == "3":
            clear_screen()
            print("\nPress ESCAPE key to return to main menu!\n\n")
            print("Initializing...\n\n")
            loading(300)
            snake_score = bonusgame()
        if maininput == "4":
            user_guide()
        if maininput == "5":
            print("Thanks for playing! :)")
            quit()

        # If no valid choice, clear screen and go back to top.
        # Also prints any scored points, if any.

        else:
            clear_screen()
            if score_count[0] > 0 or score_count[1] > 0:
                print("THE FINAL SCORE OF THIS ROUND WAS:")
                the_score_is(p1, p2, score_count[0], score_count[1])
            if int(snake_score) == 1:
                print("\nYou managed to score 1 point in snake!\n")
            if int(snake_score) > 1:
                print("\nYou managed to score {} points in snake!\n".format(snake_score))
            continue


if __name__ == "__main__":
    main()
