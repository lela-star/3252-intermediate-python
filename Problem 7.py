# Python Class 3252
# Lesson 1 Problem 7
# Author: amaops1123 (951865)

def encipher_fence(plaintext, numRails):
    '''encipher_fence(plaintext, numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    
    railcount = -1  # the starting point to create the rail
    plainchars = list(plaintext)  # the list of the characters in the plaintext
    charsinrail = []  # the list of the characters in a rail
    rails = []  # the list of the rails
    
    for i in range(numRails):
        rail = ""  # the rail itself
        railcount += 1  # each time a new rail is created, increase the starting point by 1
        charsinrail = plainchars[railcount:len(plaintext):numRails]  # use string indexing to form the rail and append them to a list
        for char in charsinrail:
            rail += char  # convert the rail from a list to a string
        rails.insert(0, rail)  # add the rail to the list of rails
        encipheredtext = ""  # the combined rails
        for item in rails:
            encipheredtext += item  # combine the rails
            
    return encipheredtext  # return the enciphered text

def decipher_fence(ciphertext, numRails):
    '''decipher_fence(ciphertext, numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    
    cipherlist = list(ciphertext)  # the ciphertext converted into a list
    raildivide = len(ciphertext) // numRails  # the biggest size of rail
    railleftover = len(ciphertext) % numRails  # the leftover characters
    rails = []  # the list of the rails
    decipheredlist = []  # the list of the deciphered characters
    decipheredtext = ""  # the deciphered text

    if railleftover >= 2:
        railstartpos = len(ciphertext) - railleftover + 1 - raildivide  # if the remainder is too big, add 1 to the starting position
    else:
        railstartpos = len(ciphertext) - railleftover - raildivide  # if the remainder is 1 or less do nothing
    railendpos = len(ciphertext)  # the first ending position

    for i in range(numRails):
        rail = cipherlist[railstartpos:railendpos]  # set the rail with a start and end position
        railendpos = railstartpos  # the old start position is now the new end position
        if railleftover > 0:
            railleftover -= 1
        if railleftover >= 1:
            railstartpos = railendpos - raildivide - 1
        else:
            railstartpos = railendpos - raildivide
        rails.append(rail)  # add the rail to the list of rails

    for i in range(raildivide + (len(ciphertext) % numRails)):
        for rail in rails:
            if i < len(rail):
                decipheredlist.append(rail[i])  # alternating between rails, add the character to the list

    for char in decipheredlist:
        decipheredtext += char  # convert the list to a string
        
    return decipheredtext  

def decode_text(ciphertext, wordfilename):
    '''decode_text(ciphertext, wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''

    file = open(wordfilename, "r")
    wordlist = file.readlines()
    file.close()
    
    for j in range(2, 11):
        cipherlist = list(ciphertext)
        raildivide = len(ciphertext) // j  # the biggest size of rail
        railleftover = len(ciphertext) % j  # the leftover characters
        rails = []  # the list of the rails
        decipheredlist = []  # the list of the deciphered characters
        decipheredtext = ""  # the deciphered text
        
        

    # steps:
    # range of 2-10
    # decode the rails
    # strip the punctuation
    # look for words that match
    # the one with the most matching words is correct

# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou
