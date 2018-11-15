# Get positve integrer

# num1 = int(input("Type a positive integrer: "))

def fizzbuzz(num1, num2):
    if num1 % 3 == 0 and num2 % 5 == 0:
        print("Fizz Buzz")
    elif num1 % 3 == 0:
        print("Fizz")
    elif num2 % 5 == 0:
        print("Buzz")
    else:
        print("Boo - your number wasn't fizz or buzz. No FizzBuzz for you!")

fizzbuzz(3, 5)
fizzbuzz(5, 9)
fizzbuzz(9, 17)
fizzbuzz(12, 53)
fizzbuzz(2, 90)
