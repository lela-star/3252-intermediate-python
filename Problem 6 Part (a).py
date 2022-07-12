# Python Class 3252
# Lesson 1 Problem 6 Part (a)
# Author: amaops1123 (951865)

f = open("wordlist.txt", "r")
count = 0

while True: 
    theline = f.readline() 
    if len(theline) == 11: 
        count += 1
    if len(theline) == 0:
        break

print(count)
f.close()
