from os import close


file = open("numbers.txt", "r")

for number in file:
    print(int(number), end=" ")

file.close()