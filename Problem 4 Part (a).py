# Python Class 3252
# Lesson 1 Problem 4 part (a)
# Author: amaops1123 (951865)

import random  # imports the random module to choose a random number

number = random.randint(0, 101)  # chooses a random number
guess = 0  # the guess itself
guessNumber = 0  # the number of guesses

print("I'm thinking of a number between 0 and 100")

while guess != number:  # while loop while the guess is wrong
    guessNumber += 1
    guess = int(input("Enter your guess: "))
    if guess < number:  # if the guess is too low
        print("Sorry,", guess, "is too low.")
    elif guess > number:  # if the guess is too high
        print("Sorry,", guess, "is too high.")

print("Good job!", guess, "is my number.")
print("It took you", guessNumber, "guesses.")
