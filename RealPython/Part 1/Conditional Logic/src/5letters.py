# Write a script that prompts the user to enter a word using the input() function, stores that input in a variable, and then displays whether the length of that string is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a set of if, elif and else statements

int = 2 #Creating infinite loop

while int > 1:
    word = input("Choose your word, pirate!")
    if len(word) == 5:
        print("It is exactly 5 characters!")
    elif len(word) < 5:
        print("It is less than five characters!")
    elif len(word) > 5:
        print("It is more than five characters!")