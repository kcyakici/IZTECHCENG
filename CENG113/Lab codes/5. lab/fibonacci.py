# sequence = int(input("Enter the number of steps you want to see in the Fibonacci sequence: "))

# if sequence < 1:
#     print("The number you enter must be at least 1")
# elif sequence == 1:
#     print("1")
# elif sequence == 2:
#     print("1 1")
# elif sequence > 2:
#     finalNumber = 1
#     previousNumber = 1
#     fibonacciList = [1, 1]
#     for i in range(sequence):
#         sumOfNumbers = previousNumber + finalNumber
#         fibonacciList.append(sumOfNumbers)
#         previousNumber = finalNumber
#         finalNumber = sumOfNumbers
#         print(fibonacciList[i], end=" ")

step = int(input("Step: "))
total = 0
n1 = 0
n2 = 1
for i in range(step-2): # assuming that first number of the sequence has the index 1
    total = n1 + n2
    n1 = n2
    n2 = total
print(total)