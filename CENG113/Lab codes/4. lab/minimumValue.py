num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
minNum = 0

if (num1 - num2) >= 0:
    minNum = num2
else:
    minNum = num1

if (minNum - num3) >= 0:
    minNum = num3

print("These are the numbers you have entered" ,num1 ,num2 ,num3)
print("This is the minimum number among them: " ,minNum)