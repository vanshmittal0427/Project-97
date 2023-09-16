

import random

print("Number guessing game")

number = random.randint(0, 20)
chances = 0

print("Guess a number (between 0 and 20):")

while chances < 5:

    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Good Job")
        break

    elif guess < number:
        print("Guess a number higher than", guess)

    else:
        print("Guess a number lower than", guess)

    chances += 1


if not chances < 5:
    print("Sorry, the number was", number)