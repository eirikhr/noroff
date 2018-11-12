# Get positve integrer

num1 = int(input("Type a positive integrer: "))

if num1 % 3 == 0 and num1 % 5 == 0:
    print("Fizz Buzz")
elif num1 % 3 == 0:
    print("Fizz")
elif num1 % 5 == 0:
    print("Buzz")
else:
    print("Boo - your number wasn't fizz or buzz. No FizzBuzz for you! It was:", str(num1))

