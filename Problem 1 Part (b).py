# Python Class 3252
# Lesson 1 Problem 1 Part (b)
# Author: amaops1123 (951865)

numAnswered = int(input("Enter the number of questions answered: "))
numCorrect = int(input("Enter the number of questions correct: "))
numBlank = (25 - numAnswered)

score = (6 * numCorrect + 1.5 * numBlank)

print("The student's score is: " + str(score))
