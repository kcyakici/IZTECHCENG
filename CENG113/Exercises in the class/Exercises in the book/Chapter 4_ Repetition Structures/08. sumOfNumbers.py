number = 1
sum = 0

while number >= 0:
    number = float(input("Enter the series of numbers: "))
    if number >= 0:
        sum = sum + number

print(sum)