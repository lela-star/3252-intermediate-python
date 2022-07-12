# Python Class 3252
# Lesson 1 Problem 6 Part (b)
# Author: amaops1123 (951865)

values = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,
          'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,
          's':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10} # the values of letters

sevenLetterWords = []  # list of seven-letter words
sevenLetterWordsWithoutZ = []  # list of seven-letter words not containing z
valuesOfWords = {}  # the values of the words
greatestValueWordSoFar = ""  # keep track of the word with the greatest value so far

def calculate_value(word):
    '''calculate_value(word) -> int
    returns the scrabble value of a word'''
    value = 0
    wordChars = list(word)
    for char in wordChars:
        value += values[char]
    return value
        

f = open("wordlist.txt", "r")  # open the file

while True:  # while loop to check each line
    theline = f.readline()
    if len(theline) == 8: 
        sevenLetterWords.append(theline)
    if len(theline) == 0:
        break

for word in sevenLetterWords:  # for loop to remove the \n character
    wordChars = list(word)
    wordChars.pop(-1)
    newWord = ""
    isThereZ = False
    for char in wordChars:  # for loop to check if z is in the word
        newWord += char
        if char == "z":
            isThereZ = True
    if isThereZ == False:  # if z is not in the word, append it to the list
        sevenLetterWordsWithoutZ.append(newWord)

greatestValueWordSoFar = sevenLetterWordsWithoutZ[0]  

for word in sevenLetterWordsWithoutZ:  # for loop to determine the word with the greatest value
    if calculate_value(word) >= calculate_value(greatestValueWordSoFar):
        greatestValueWordSoFar = word

print(greatestValueWordSoFar)
