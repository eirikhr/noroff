import random

correct = random.randint(1, 20)
count = 0
# print("Correct answer:", correct)

while True:
    guess = input("What is your guess? ")
    count += 1
    try:
        if guess.lower() == "q" or guess.lower() == "quit":
            print("Ok, we're done :)")
            break
        if int(guess) == correct:
            if count < 2:
                print("Holy shit you guessed it! It only took you one time to get it right!")
            elif count < 3:
                print("Holy shit you guessed it! It only took you", count, "times to get it right!")
            elif count < 10:
                print("Holy shit you guessed it! It took you", count, "times to get it right!")
            elif count > 10:
                print("You guessed it! It took you", count, "times to get it right! Not really good to be honest ;)")
            print("Thanks for playing :)")
            break
    except ValueError:
        print("That is not an integrer.")
    else:
        print("That is incorrect. You have guessed", count, "times")
        continue