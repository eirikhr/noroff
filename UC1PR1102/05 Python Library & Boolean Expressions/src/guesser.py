import random

correct = random.randint(0, 20)
count = 0
print("Correct answer:", correct)

while True:
    guess = input("What is your guess? ")
    count += 1
    if guess.lower == "q":
        print("Ok, we're done :)")
        break
    if int(guess) == correct:
        if count < 2:
            print("Holy shit you guessed it! It only took you", count, "time to get it right!")
        if count < 3:
            print("Holy shit you guessed it! It only took you", count, "times to get it right!")
        if count < 10:
            print("Holy shit you guessed it! It took you", count, "times to get it right!")
        if count > 3:
            print("Holy shit you guessed it! It only took you", count, "times to get it right!")
        print("Thanks for playing")
        break
    else:
        print("That is incorrect. You have guessed", count, "times")
        continue