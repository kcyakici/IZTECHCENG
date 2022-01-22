import string
import random as rd
import time

def main():

    print("Welcome to the random password generator\nThe program can create passwords with three different security levels")
    print("Level 1: A password of length 4, consisting of only integers.\nLevel 2: A password of length 8, consisting of digits and lowercase letters")
    print("Level 3: A password of length 12, consisting of digits, lowercase and uppercase letters and special characters")

    
    invalidInput = True
    while invalidInput:

        userInput = input("Please enter a level of which you want your password security to be: ")

        if userInput != "1" and userInput != "2" and userInput != "3":

            print("Please enter either 1, 2 or 3")

        else:

            invalidInput = False
            password = generateRandomPassword(userInput)

            print(f"This is the password generated: {password}")

            elapsedTime = getElapsedTime(userInput)
            print(f"This is the elapsed time to run the function: {elapsedTime}")

def generateRandomPassword(securityLevel):
    
    password = ""
    if securityLevel == "1":

        for i in range(4):
            selection = rd.randint(0, 9)
            password = password + str(selection)

    elif securityLevel == "2":

        selectionList = string.ascii_lowercase + string.digits
        for i in range (8):
            selection = rd.choice(selectionList)
            password = password + selection

    elif securityLevel == "3":

        selectionList = string.ascii_letters + string.digits + string.punctuation
        for i in range(12):
            selection = rd.choice(selectionList)
            password = password + selection

    return password

def getElapsedTime(userInput):

    startingTime = time.perf_counter()
    generateRandomPassword(userInput)
    endingTime = time.perf_counter()

    return (endingTime - startingTime)

main()
