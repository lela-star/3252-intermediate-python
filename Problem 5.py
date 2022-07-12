# Python Class 3252
# Lesson 1 Problem 5
# Author: amaops1123 (951865)

def remove_letter(string, letter):
    '''remove_letter(string, letter) -> str
    returns string with all occurrences of letter removed'''
    
    indexesToPop = []  # the list of the indexes to pop
    listOfCharacters = list(string)  # the list of the characters in the string
    indexCount = -1  # the count of the indexes to pop
    characterCount = 0  # the account of the length of the string
    finalString = ""  # the final string to output
    
    for character in string:  # find the indexes to pop
        indexCount += 1
        if character == letter:
            indexesToPop.append(indexCount)
            
    for index in indexesToPop:  # pop the indexes
        listOfCharacters.pop(index - characterCount)
        characterCount += 1
        
    for character in listOfCharacters:  # assemble the final string
        finalString += character
        
    return finalString

# test cases
print(remove_letter('This is a test','t'))  # should print 'This is a es'
print(remove_letter('Hello World!','l'))    # should print 'Heo Word!'
print(remove_letter('I like Python','q'))   # should print 'I like Python'
