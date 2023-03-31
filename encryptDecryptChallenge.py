# https://stackabuse.com/python-check-if-a-file-or-directory-exists/
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python


import os
import random

def encrypt(message, password):
    #Set the random seed so that the random number generator returns the same number every time
    random.seed(password)
    res = ""

    #For every character add a random interger to the string
    for char in message:
        res += char + str(random.randint(0, 9))
    return res


def decrypt(message, password):
    random.seed(password)
    res = ""
    i = 0

    #Every two characters generate a random number using the seed from the password, if the random number
    for char in message:
        if i % 2 != 0:
            if char != str(random.randint(0, 9)):
                res += char
        else:
            res += char
        i += 1

    return res


def encryptFile(fileName, newFileName, password):
    #Try opening both files and return false if file can't be opened
    try:
        file = open(fileName, "r")
        newFile = open(newFileName, "w")
    
    except FileNotFoundError:
        return False
    
    #Encrypt text
    encrypted = encrypt(file.read(), password)

    #Write text into a new file
    for line in encrypted:
        newFile.write(line)

    file.close()
    newFile.close()

    #Remove original file
    os.remove(fileName)
    
    #Return string
    return encrypted


def decryptFile(fileName, newFileName, password):
    #Try opening both files and return false if file can't be opened
    try:
        file = open(fileName, "r")
        newFile = open(newFileName, "w")
    
    except FileNotFoundError:
        return False

    #Decrypt text
    decrypted = decrypt(file.read(), password)

    #Write text into a new file
    for line in decrypted:
        newFile.write(line)

    file.close()
    newFile.close()

    return decrypted


print("Welcome to Tomas' amazing file encrypt decrypt program!")
print("Commands are: 'c' for close, 'e' for encrypt and 'd' for decrypt")

while True:
    command = input("\nEnter Command: ").lower()
    print("")

    if command == "e":
        fileName = input("Encrypt: ")

        pass1 = input("Enter password: ")
        pass2 = input("Confirm password: ")

        #If passwords don't match, pass
        if pass1 != pass2:
            print(" Passwords don't match. Please try again.")
            pass

        #If either file is invalid, pass
        if not encryptFile(fileName, "encrypted.txt", pass1):
            print("Invalid file name. Please try again.")
            pass
        else:
            print("\n" + fileName + " has been encrypted as a new file encrypted.txt")
            print(fileName + " has been deleted.")

    elif command == "d":
        fileName = input("Decrypt: ")

        pass1 = input("Enter password: ")

        #If either file is invalid pass
        if not decryptFile(fileName, "decrypted.txt", pass1):
            print("Invalid file name. Please try again.")
            pass
        else:
            print(fileName + " has been decrypted as a new file decrypted.txt")

    elif command == "c":
        break

    #If command isn't valid
    else:
        print("Not a valid command")
        print("Commands are: 'c' for close, 'e' for encrypt and 'd' for decrypt \n")