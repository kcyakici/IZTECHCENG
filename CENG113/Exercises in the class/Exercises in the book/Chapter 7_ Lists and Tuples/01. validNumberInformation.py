numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

validNumbers = []

for number in numbers: 
    if number > 0 and number < 100:
        validNumbers.append(number)

sumOfTheList = sum(validNumbers)
averageOfTheList = (sumOfTheList / len(validNumbers))

print(f"This is the list of valid numbers: {validNumbers}\nThis is the sum of the elements in the list: {sumOfTheList}\nThis is the average of the numbers in the list: {averageOfTheList}")
