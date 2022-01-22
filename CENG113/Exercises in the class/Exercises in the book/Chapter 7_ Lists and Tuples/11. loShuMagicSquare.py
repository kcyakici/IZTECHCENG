def isMagicSquare(square):
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in square:
        for column in row:
            if column in numberList:
                numberList.remove(column)
    if len(numberList) > 0:
        return False
    
    summationOfRowsList = []
    for row in square:
        summationOfRow = 0
        for column in row:
            summationOfRow = summationOfRow + column
        summationOfRowsList.append(summationOfRow)
    
    for i in range(len(summationOfRowsList)):
        for j in range(i + 1, len(summationOfRowsList)):
            if summationOfRowsList[i] != summationOfRowsList[j]:
                return False

    summationOfColumnsList = []
    for j in range(len(square)):
        summationOfColumn = 0
        for i in range(len(square)):
            summationOfColumn = summationOfColumn + square[i][j]
        summationOfColumnsList.append(summationOfColumn)

    for i in range(len(summationOfColumnsList)):
        for j in range(i + 1, len(summationOfColumnsList)):
            if summationOfColumnsList[i] != summationOfColumnsList[j]:
                return False

    diagonal1 = 0
    for i in range(len(square)):
        diagonal1 = diagonal1 + square[i][i]

    diagonal2 = 0
    for i in range(len(square)):
        diagonal2 = diagonal2 + square[len(square) - 1 - i][i]
    
    if diagonal1 != diagonal2 or diagonal2 != summationOfColumn or summationOfColumn != summationOfRow:
        return False
    
    return True

def main():

    M = [[4,9,2],[3,5,7],[8,1,6]]

    print(isMagicSquare(M))

if __name__ == "__main__":
    main()