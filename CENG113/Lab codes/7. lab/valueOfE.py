steps = int(input("Enter the number of steps in the series of which you want to find an approximation: "))

if steps == 1:
    e = 1
elif steps > 1:
    e = 1
    for i in range(steps-1):
        denominator = 0
        term = 1
        for denominator in range(1, i+2):
            temp = (1/denominator)
            term = temp * term
        e = term + e
print("Approximation of e is",e)