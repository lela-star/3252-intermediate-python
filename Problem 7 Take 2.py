# Python Class 3252
# Lesson 1 Problem 7
# Author: amaops1123 (951865)

def encipher_fence(plaintext, numRails):
    '''encipher_fence(plaintext, numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    
    railcount = -1  # the starting point to create the rail
    plainchars = list(plaintext)
    charsinrail = []
    rails = []
    
    for i in range(numRails):
        # creates one rail per iteration
        rail = ""
        railcount += 1
        charsinrail = plainchars[railcount:len(plaintext):numRails]
        for char in charsinrail:
            # converts the rail from a list to a string
            rail += char
        rails.insert(0, rail)
        encipheredtext = "" 
        for item in rails:
            # combines the list of rails into the enciphered text
            encipheredtext += item
            
    return encipheredtext  # return the enciphered text

def decipher_fence(ciphertext, numRails):
    '''decipher_fence(ciphertext, numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''

    cipherchars = list(ciphertext)
    cipherlength = len(ciphertext)
    raillengths = []
    smallrail = cipherlength // numRails  # smallest size of rail (integer division)
    railleftover = cipherlength % numRails  # leftover chars (remainder)
    count = cipherlength
    rails = []
    decipheredtext = ""  # deciphered text with placeholders
    finaltext = ""  # placeholder chars removed

    while count > smallrail * railleftover + railleftover:
        # creates the small rails and appends them to raillengths
        raillengths.append(smallrail)
        count -= smallrail
    for i in range(railleftover):
        # distributes railleftover among other rails
        raillengths.append(smallrail + 1)
        count -= smallrail + 1
    raillengths.append(0)  # eliminates the 'list index out of range' error
    startposition = 0
    endposition = raillengths[0]
    for i in range(numRails):
        # creates the rails themselves
        rails.insert(0, cipherchars[startposition:endposition])
        startposition = endposition
        endposition += raillengths[i + 1]
    for rail in rails:
        # evens out the rails, once again, to eliminate the 'list index out of range' error
        if len(rail) == smallrail and railleftover != 0:
            rail += "|"  # placeholder character
    extra = 0  # to account for the extra character in the large rail and also to eliminate the 'list index out of range' error'
    if railleftover != 0:
        extra = 1
    for i in range(smallrail + extra):
        # deciphers the ciphertext
        for rail in rails:
            raillist = list(rail)
            decipheredtext += raillist[i]
    decipheredlist = list(decipheredtext)
    difference = 0
    for i in range(len(decipheredtext)):
        # removes the placeholder characters
        if decipheredlist[i - difference] == "|":
            decipheredlist.pop(i - difference)
            difference += 1
    for item in decipheredlist:
        # combines the characters in decipheredlist into the final text
        finaltext += item
        
    return finaltext

def decode_text(ciphertext, wordfilename):
    '''decode_text(ciphertext, wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''

    file = open(wordfilename, "r")
    decodes = []
    decodedtext = ""
    punctuation = "!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    words = []
    count = -1
    highscore = 0
    highcount = 0

    while True:
        # gather all the words into a list
        word = file.readline()
        if len(word) == 0:
            break
        wordchars = list(word)
        wordchars.pop(-1)
        newword = ""
        for char in wordchars:
            # converts wordchars from a list to a string
            newword += char
        words.append(newword)
    file.close()
    for i in range(2, 11):
        # deciphers the ciphertext
        decodes.append(decipher_fence(ciphertext, i))
    for decode in decodes:
        # goes through all the decodes
        cleandecode = ""
        lowerdecode = ""
        splitdecode = []
        validity = 0
        count += 1
        for letter in decode:
            # removes the punctuation
            if letter not in punctuation:
                cleandecode += letter
        lowerdecode = cleandecode.lower()  # puts the decode in lowercase
        splitdecode = lowerdecode.split()  # removes whitespace from the decode
        for word in splitdecode:
            # checks how many valid words are in the decode
            if word in words:
                validity += 1
        if validity >= highscore:
            highscore = validity
            highcount = count
            
    decodedtext = decodes[highcount]
    return decodedtext
                
# test cases

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
        
