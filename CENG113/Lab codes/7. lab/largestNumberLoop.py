print("Enter the series of non-negative numbers to find the maximum among them")
print("Enter 0 or a negative number to print the result and end the program")
userInput = 1
maxValue = 0
while userInput > 0:
    userInput = float((input("Enter the number: ")))
    if userInput > maxValue:
        maxValue = userInput

print("The maximum number among the given numbers is",maxValue)