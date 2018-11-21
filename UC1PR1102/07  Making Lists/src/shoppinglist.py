def getitem(printstring=""):
    printstring = str(printstring)
    if len(printstring) > 0:
        print(printstring)
    value = input("-> ")
    if value.lower() == "q" or value.lower() == "quit":
        print("Goodbye")
        quit()
    return value


shopping_list = []


while True:
    entry = getitem("Enter your Item")
    if entry != "end":
        shopping_list.append(entry)
    else:
        print(shopping_list)
        break
