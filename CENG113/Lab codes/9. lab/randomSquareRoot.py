import random as rd

# M = [[9, 16, 25], [36, 49, 64]]

# def getRandomSquareRoot(M):
    
#     randomRow = rd.choice(M)
#     randomColumn = rd.choice(randomRow)
#     squareRoot = randomColumn ** (1/2)

#     return randomColumn, squareRoot

# def main():

#     randomColumn, squareRoot = getRandomSquareRoot(M)

#     print(f"This is the number chosen from the list: {randomColumn}\nThis is the square root of the number: {squareRoot}")

# main()

print("Enter the rows and columns of the matrix\nFirst enter the values in a row one by one\nWhen a row is completed, type 'r' to show that the current row is completed\nType 'q' to finish adding numbers")


def getMatrix():
    M = []
    R = []
    firstRowEntered = False # using it because matrix will have a fixed number of columns after the first row is given
    elementsInRow = 0
    programIsRunning = True
    while programIsRunning:
        if not firstRowEntered:
            row = input("Enter the numbers one by one: ")

            if row.isnumeric():
                row = int(row)
                R.append(row)
                elementsInRow += 1

            elif row == "r":
                M.append(R)
                if not firstRowEntered:
                    fixedColumn = elementsInRow
                    firstRowEntered = True

            elif row == "q":
                programIsRunning = False
                return M

            else:
                print("Error! Enter a numerical value!")
        
        else:
            print(f"This is the last row you have entered: {R}")
            R = []
            while len(R) != fixedColumn:
                row = input("Enter the numbers one by one:")

                if row.isnumeric():
                    row = int(row)
                    R.append(row)

                elif row == "q":
                    programIsRunning = False
                    return M

                else:
                    print("Error! Enter a numerical value!")
            
                if programIsRunning:
                    M.append(R)
        

def getRandomSquareRoot(M):
    
    randomRow = rd.choice(M)
    randomColumn = rd.choice(randomRow)
    squareRoot = randomColumn ** (1/2)

    return randomColumn, squareRoot

def main():

    M = getMatrix()

    randomColumn, squareRoot = getRandomSquareRoot(M)

    print(f"This is the number chosen from the list: {randomColumn}\nThis is the square root of the number: {squareRoot}")

main()