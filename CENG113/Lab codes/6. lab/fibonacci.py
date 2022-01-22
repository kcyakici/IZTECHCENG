sequence = int(input("Enter the number of steps you want to see in the Fibonacci sequence: "))

if sequence < 1:
    print("The number you enter must be at least 1")
elif sequence == 1:
    print("1")
elif sequence == 2:
    print("1 1")
elif sequence > 2:
    finalNumber = 1
    previousNumber = 1
    fibonacciList = [1, 1]
    for i in range(sequence):
        sumOfNumbers = previousNumber + finalNumber
        fibonacciList.append(sumOfNumbers)
        previousNumber = finalNumber
        finalNumber = sumOfNumbers
        print(fibonacciList[i], end=" ")
