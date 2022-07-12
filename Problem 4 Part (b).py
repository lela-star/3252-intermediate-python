# Python Class 3252
# Lesson 1 Problem 4 part (b)
# Author: amaops1123 (951865)

import random  # imports the random module to choose a random number

low = 0  # the lower limit
high = 101  # the higher limit
guess = random.randint(low, high)  # the first guess
guessNumber = 0  # the number of guesses
position = ""  # high, low or correct?

print("Think of a number between 0 and 100.")
input("Hit enter when you have it.")

while position != "correct":  # while loop while the position is low or high
    guessNumber += 1
    print("I guess,", guess)
    position = input("Is this high, low, or correct? ")
    if position == "low":  # if the guess is too low, set the lower limit
        low = guess
    elif position == "high":  # if the guess is too high, set the higher limit
        high = guess - 1
    guess = random.randint(low, high)  # guess with the new limits

print("I knew it!")
print("It took me", guessNumber, "guesses.")
