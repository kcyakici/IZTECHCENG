gpa = float(input("Please enter your GPA: "))
lectureNumber = int(input("Please enter the number of lectures you have gotten: "))

if gpa < 2 and lectureNumber < 47:
    print("Not enough number of lectures, and GPA is not satisfactory")
elif gpa < 2 and lectureNumber >= 47:
    print("GPA is not satisfactory")
elif gpa >= 2 and lectureNumber < 47:
    print("Not enough number of lectures")
elif gpa >= 2 and lectureNumber >= 47:
    print("GRADUATED!")