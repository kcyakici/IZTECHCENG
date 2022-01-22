def average(studentGradeList):
    
    weight = [[0.3], [0.3], [0.4]]
    weighedList = []

    k = 0
    for i in range(len(studentGradeList)):

        weighedGrade = 0
        for j in range(len(weight)):

            weighedGrade = weighedGrade + weight[j][k] * studentGradeList[i][j]
        
        weighedList.append(weighedGrade)

    return weighedList

        

def main():

    studentsAreBeingAdded = True
    studentsList = []

    while studentsAreBeingAdded:

        studentGrades = []

        midterm1 = int(input("Enter first midterm grade: "))
        studentGrades.append(midterm1)
        midterm2 = int(input("Enter second midterm grade: "))
        studentGrades.append(midterm2)
        final = int(input("Enter final grade: "))
        studentGrades.append(final)

        studentsList.append(studentGrades)
        
        userAnswer = input("Do you want to continue? (y/n): ")

        if userAnswer == "n":

            studentsAreBeingAdded = False
    
    weighedList = average(studentsList)

    print(weighedList)

if __name__ == "__main__":
    main()
