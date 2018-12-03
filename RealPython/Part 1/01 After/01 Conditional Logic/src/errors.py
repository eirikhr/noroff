while True:
    try:
        number = int(input("Enter an int: $> "))
        number = int(number)
        print("You did it!")
    except ValueError:
        print("That was not an integrer. Try again.")

print("You made it to the end!")

