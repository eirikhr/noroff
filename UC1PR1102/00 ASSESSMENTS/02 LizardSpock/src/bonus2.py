"""
bonus2.py
Eirik Rynning 2018
"""


import random
import LizardSpock


WORDS = "words.txt"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_input(printstring=""):
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
    if value.lower() == "quit":
        print("Thanks for playing :)")
        quit()
    return value



def get_word(maxlength):
    """Get random word from word list

    Args
        maxlength (int): Maximum length of the word this function should return.

    Returns:
        Randomly selected word from WORDS, but not longer than maxlength.
    """
    selected_words = []

    with open(WORDS, "r") as i:  # Open wordlist in reading mode, and perform:
        for word in i:
            if len(word) > maxlength:  # Don't pick words over the maximum length
                continue
            selected_words.append(word)  # Add qualified words to list.
    return random.choice(selected_words)  # Pick random word from list.


def get_length():
    """Get maximum length from user."""
    while True:
        max_length = get_input("Please input the maximum length of the word you want to guess [4-16]:")
        try:
            max_length = int(max_length)
            if 4 <= max_length <= 16:
                return max_length
            else:
                print("{} is not an integrer between 4 and 16.\n" .format(max_length))
        except ValueError:
            print("{} is not an integrer between 4 and 16.\n" .format(max_length))


def get_attempts():
    """Get maximum attempts from user."""
    while True:
        attempts = get_input("Please input the maximum incorrect attemps you want to have [1-25]:")
        try:
            attempts = int(attempts)
            if 1 <= attempts <= 25:
                return attempts
            else:
                print("{} is not an integrer between 1 and 25.\n".format(attempts))
        except ValueError:
            print("{} is not an integrer between 1 and 25.\n".format(attempts))


def hide_word(word, hidden_word):
    """Hide unguessed characters in the word
    Args:
        word (str): The actual word user needs to guess.
        hidden_word (list): A list of booleans. One entry per character in word.
                            Booleans with True value are to be shown, and False will be hidden

    Returns:
        replaced (str): If word is "HELLO" and LL in hidden_word is True, it will return as
                        "**LL*"

          """
    replaced = "".join([letter if hidden_word[i] else "*" for i, letter in enumerate(word)])
    return replaced


def get_guess(remaining):
    """Get the next guess"""
    while True:
        letter = get_input("Guess the next letter:")
        letter = letter.lower()  # Parse everything as lowercase.
        if len(letter) != 1:
            print("{} is not a single letter.\n"
                  "You can only guess one letter at the time".format(letter))
        elif letter not in alphabet:
            print("{} is not a letter.\n".format(letter))
        elif letter not in remaining:
            print("{} has already been guessed.\n".format(letter))
        else:
            LizardSpock.clear_screen()
            # Remove the guessed letter from remaining letters that can be guessed
            remaining.remove(letter)
            return letter


def main():
    """Start the main game loop."""
    LizardSpock.loading()
    print("Welcome to Guess the word!")
    attempts = get_attempts()
    max_length = get_length()
    print("Getting a random word...")
    LizardSpock.loading()
    word = get_word(max_length)
    # print(word)  # For testing

    # Initializing variables
    hidden_word = [letter not in alphabet for letter in word]
    guessed_letters = []  # Correctly guessed letters
    remaining = set(alphabet)  # Creates a set of all letters remaining.  {'a', 'b', } --- and so on
    solved = False

    while attempts > 0 and not solved:
        # LizardSpock.clear_screen()
        print("Word:\n {}".format(hide_word(word, hidden_word)).upper())
        print("Attempts left:\n\n {}\n".format(attempts))
        print("Guessed letters:\n\n {}\n\n".format("".join(guessed_letters)))

        # Get guess
        guess = get_guess(remaining)
        LizardSpock.loading()

        # Check if guess is in the word
        if guess in word:
            print("Sweet! {} is in the word!\n".format(guess.upper()))

            for i in range(len(word)):
                if word[i] == guess:
                    # Make the boolean in the list of correct letters True
                    # That way, it will reveal itself.
                    hidden_word[i] = True

        else:
            print("Unfortunately, {} is not in the word!\n".format(guess.upper()))
            attempts -= 1
            guessed_letters.append(guess)  # Add incorrect letter to guessed letter list.

        # Check if word is solved

        if False not in hidden_word:
            solved = True

    if solved:
        print("You won the game!!")
        print("The word was {}".format(word.upper()))
        input("press enter to continue...")

    else:
        print("You lost the game this time :(")
        print("The word was {}".format(word.upper()))
        input("press enter to continue...")


if __name__ == "__main__":
    main()
