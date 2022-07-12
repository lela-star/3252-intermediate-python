# Python Class 3252
# Lesson 1 Problem 3
# Author: amaops1123 (951865)

global properdivisors  # the sum of the number's proper divisors
properdivisors = 0

for n in range(100, 1000):  # while loop for going through all the three-digit numbers
    properdivisors = 0  # reset the sum of the proper divisors
    for d in range (1, n):  # for loop to go through the proper divisors
        if n % d == 0:  # check if the number is a divisor
            properdivisors += d  # if so, add the number to the sum
    if properdivisors == 2*n:  # print the double-perfect numbers
        print(n)
            
