with open("06numbers.txt", "r") as f:
    content = f.readlines()

summation = 0
count = 0
for line in content:
    line = line.split()
    for number in line:
        number = int(number)
        summation = summation + number
        count += 1

print(summation / count)
