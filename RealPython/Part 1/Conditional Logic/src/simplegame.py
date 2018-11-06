while True:  # Well now we've got to find the quit()
    print("Try to get 4 or less than 15!")
    no1 = input("Number 1: ")
    no2 = input("Number 2: ")
    if int(no1) + int(no2) == 4:
        print("2 and 2 is in fact 4!")
        print("Yay! You found the quit()")
        quit()
    elif int(no1) + int(no2) == 7:
        print("You picked 7? Seriously? \nNope. I wont let you quit using CR7's jersey number!\nTry again!")
    elif int(no1) + int(no2) < 15:
        print("{} and {} is  less than 15!".format(no1, no2))
        print("You rock!")
        quit()
    else:
        print("{} and {} is not 4 or less than 15".format(no1, no2))
        print()
        print("You were wrong!")
        print("Cant let you off the hook yet!")
