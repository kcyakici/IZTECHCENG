i=0
lastMessage = ""

while i < 3:
    if i < 2:
        name, surname, grade = input("Please enter the name, surname and the grade of the student, respectively: ").split()
        message = str(name + " " + surname + " got " + grade + ",")
        lastMessage = lastMessage + message + " "
        i = i + 1
    else:
        name, surname, grade = input("Please enter the name, surname and the grade of the student, respectively: ").split()
        message = str("and " + name + " " + surname + " got " + grade + " from the course.")
        lastMessage = lastMessage + message
        break

print(lastMessage)