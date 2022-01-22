char = "#"
space = " "
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    print(char, end="")
    for j in range(i):
        print(space, end="")
    print(char)