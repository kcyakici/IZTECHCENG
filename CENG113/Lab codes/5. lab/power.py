base = int(input("Please enter the base number: "))
power = int(input("Please enter the power: "))

baseNumber = base

if power == 0:
    print(base,"to the power of",power,"is 1")
if power != 0:
    if power > 0:
        for i in range (power - 1):
            baseNumber = base * baseNumber
    elif power < 0:
        for i in range (-1 * (power) - 1):
            baseNumber = base * baseNumber
        baseNumber = 1 / baseNumber
    print(base,"to the power of",power,"is",baseNumber)