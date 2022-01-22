import random as rd

userInput = int(input("How many random numbers would you like in the file? "))

with open("07randomNumberText.txt", "w") as f:
    for i in range (userInput):
        randomNumber = rd.randint(1,500)
        randomNumber = str(randomNumber)
        f.writelines(randomNumber + " ")

with open("07randomNumberText.txt", "r") as f:
    content = f.readlines()


for line in content:
    line = line.split()
    for number in line:
        print(number, end=" ")