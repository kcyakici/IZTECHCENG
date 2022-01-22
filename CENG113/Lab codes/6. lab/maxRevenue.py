M = [[1,3,5,4,2],[3,2,4,2,1]]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for j in range(len(M[0])):
    dayRevenue = 0
    for i in range(len(M)):
        dayRevenue = dayRevenue + M[i][j]
    print("The revenue for",days[j],"is",dayRevenue,"$") 
        
# transpose = []
# for j in range(len(M[0])):
#     columnsAsRow = []
#     for i in range(len(M)):
#         columnsAsRow.append(M[i][j])
#     transpose.append(columnsAsRow)

# print(transpose)