numberList = []

for i in range(20):
    number = int(input("Enter a number: "))
    numberList.append(number)

total = sum(numberList)
average = total / 20
highest = max(numberList)
lowest = min(numberList)

print(total, average, highest, lowest)