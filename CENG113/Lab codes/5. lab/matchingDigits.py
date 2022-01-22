number = list(input("Enter the first number: "))
number2 = list(input("Enter the second number: "))
matchingDigits = 0

lenghtOfNumber = len(number)
lengthOfNumber2 = len(number2)

if lenghtOfNumber >= lengthOfNumber2:
    for i in range(lengthOfNumber2): # frag mal ob eine bessere Möglichkeit anstatt "i" vorkommen konnte
        if number2[lengthOfNumber2 - i - 1] == number[lengthOfNumber2 - i - 1]:
            matchingDigits = matchingDigits + 1
elif lenghtOfNumber < lengthOfNumber2:
    for i in range(lenghtOfNumber + 1):
        if number[lenghtOfNumber - i - 1] == number2[lenghtOfNumber - i - 1]:
            matchingDigits = matchingDigits + 1
print("The total number of matching digits is",matchingDigits)