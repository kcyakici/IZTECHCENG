fileName = input("Enter the name of the file to check the contents: ")

file = open(fileName, "r")
lineCount = 1
for line in file:
    
    print(f"#{lineCount}: line.rstrip(\n)")
    
file.close()