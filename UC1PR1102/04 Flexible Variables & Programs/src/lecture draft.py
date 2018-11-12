import random

#num1 = int(input("Input number 1: "))
#num2 = int(input("Input number two: "))


def addition(x,y):
    return x + y


def subtraction(x, y):
    return x - y


def multiply(x, y):
    return x * y


def givec(x):
    return 5/9 * (x - 32)


def givef(x):
    return 9/5 * x + 32

"""
print("Addition = ", addition(num1, num2))
print("Subtraction = ", subtraction(num1, num2))
print("Multiply = ", multiply(num1, num2))

"""

while True:
    print()
    num1 = input("Input number 1: ")
    print()
    if len(num1) == 0:
        print("Ok, then I won't ask you for the input")
        num1 = int(random.randint(1,100))
        print("I'll calculate my favorite number,", num1, "instead :)" )
        print(num1, "degrees F to Celcius: ", givec(num1))
        print(num1, "degrees C to Fahrenheit: ", givef(num1))
    else:
        print(num1, "degrees F to Celcius: ", givec(int(num1)))
        print(num1, "degrees C to Fahrenheit: ", givef(int(num1)))

