# Python Class 3252
# Lesson 1 Problem 2
# Author: amaops1123 (951865)

global digits  # the digits in the three-digit number
global squaresum  # the sum of the squares of the digits
global quotient  # the result of dividing n by 11

digits = []
squaresum = 0
quotient = 0

for n in range(100, 1000):  # while loop for going through all the numbers
    if n % 11 == 0:  # check if the number is divisible by 11
        n = str(n)
        digits = [int(n[0]), int(n[1]), int(n[2])]  # list the digits of the number
        squaresum = digits[0]**2 + digits[1]**2 + digits[2]**2  # calculate the sum of its squares
        quotient = int(n)/11  # divide the number by 11
        if squaresum == quotient:  # print the numbers that correspond to the criteria
            print(n)
        
