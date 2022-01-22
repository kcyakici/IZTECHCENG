fileName = input("Enter the name of the file to check the contents: ")

file = open(fileName, "r")
lineCount = 0
for line in file:
    print(line.rstrip("\n"))
    lineCount += 1
    if lineCount == 5:
        break
    
file.close()