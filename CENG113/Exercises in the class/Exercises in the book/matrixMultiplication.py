M1 = [[3,6,9],
    [2,5,8]]

M2 = [[1,5,9,5],[3,5,7,5],[8,5,2,5]]

resultMatrix = []

for i in range(len(M1)):
    row = []
    for k in range(len(M2[0])):
        result = 0
        for j in range(len(M2)):
            element1 = M1[i][j]
            element2 = M2[j][k]
            result = result + element1 * element2
        row.append(result)
    resultMatrix.append(row)

print(resultMatrix)
            