numberOfIntegers = int(input("How many numbers will you enter? "))
numberOfEvens = 0

for i in range(numberOfIntegers):
    number = (int(input("Enter an integer: ")))
    if number%2 == 0:
        numberOfEvens = numberOfEvens + 1
print("The percentage of the even numbers in the total numbers given is", (numberOfEvens / numberOfIntegers) * 100, "%")