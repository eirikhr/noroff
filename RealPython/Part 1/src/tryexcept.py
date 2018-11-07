"""

while True:
    try:
        number = int(input("Enter an integer: "))
        print("The number is", number)
    except ValueError:
        print("That was not an integrer")

"""

def divide(num1, num2):
    print(num1 / num2)

while True:
    try:
        divide(int(input("Type the first number: ")), int(input("Type the second number: ")))
    except ValueError:
        print("That was not an integrer")
    except ZeroDivisionError:
        print("You cannot divide anything by 0!")
