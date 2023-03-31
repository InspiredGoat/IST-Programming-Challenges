# Pokemon challenge was harder...
# https://stackoverflow.com/questions/8254477/looping-for-every-character-in-a-string-in-python-decoder-ring#8254662

import string

#Rewrote string.ascii_uppercase to chars for faster, sleaker and more sensible notation which not only makes the program look nicer but it also makes it faster to code I love writing comments
chars = string.ascii_uppercase

#Turns character into index inside the chars array
def getCharIndex(char):
    for i in range(len(chars)):
        #If the character equals the array at the index, return the index
        if char == chars[i]:
            return i

    #If the key has any symbols, spaces or invalid stuff return false
    return False

def makeTable(message):
    table = []
    #Creates table by adding all the character indecies to be used as offsets later
    for char in message:
        charIndex = getCharIndex(char)
        
        #If character is a valid character, add it to the table
        if char in chars:
            table.append(charIndex)
    return table

#Gets rid of numbers and symbols
def fixMessage(message):
    res = ""
    for char in message:
        #If the character is in the alphabet append it to the array
        if char.upper() in chars:
            res += char
    return res

#Wrap function wraps the value around max using the modulo operator
def wrap(i, max):
    return i % max

def encrypt(message, key):
    message = fixMessage(message.upper())
    table = makeTable(key)
    res = ""

    #Loop through every character in message
    for i in range(len(message)):
        charIndex = getCharIndex(message[i])
        
        #If character index is invalid, skip it
        if not charIndex:
            pass

        #Adds the character index to the coresponding table index to find the value and wraps that around the chars array to find the correct character index 
        index = wrap(charIndex + table[wrap(i, len(table))], len(chars))

        #Add character to result
        res += chars[index]
    
    return res

#Literally identical to encrypt except for one symbol!
def decrypt(message, key):
    message = fixMessage(message.upper())
    table = makeTable(key)
    res = ""

    #Loop through every character in message
    for i in range(len(message)):
        charIndex = getCharIndex(message[i])
        
        #If character index is invalid, skip it
        if not charIndex:
            pass
        
        #Removes the character offset to revert the encryption 
        index = wrap(charIndex - table[wrap(i, len(table))], len(chars))

        #Add character to result
        res += chars[index]
    
    return res


print("Welcome to Tomas' amazing python vigenere cipher program!")
print("Commands are: 'c' for close, 'e' for encrypt and 'd' for decrypt")

while True:
    command = input("\nEnter command: ")
    print("")

    #Exit loop if command is c    
    if command == 'c':
        break

    #Encrypt message and print result
    elif command == 'e':
        key = input("Enter key: ").upper()
        message = input("Enter message to encrypt: ")
        print(encrypt(message, key))

    #Dencrypt message and print result
    elif command == 'd':
        key = input("Enter key: ").upper()
        message = input("Enter message to decrypt: ")
        print(decrypt(message, key))

    #If it isn't a command, remind the user what the valid commands are
    else:
        print("Not a valid command")
        print("Commands are: 'c' for close, 'e' for encrypt and 'd' for decrypt \n")
