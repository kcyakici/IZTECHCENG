rainfallList = []

for i in range(12):
    rainfall = int(input("Enter the rainfall for the month: "))
    rainfallList.append(rainfall)

sumOfRainfall = sum(rainfallList)
lowestRainfall = min(rainfallList)
highestRainfall = max(rainfallList)
averageRainfall = sumOfRainfall / 12

print(f"Rainfall list: {rainfallList}")
print(f"This is the sum of the rainfalls: {sumOfRainfall}\nThis is the lowest of the rainfalls: {lowestRainfall}")
print(f"This is the highest of the rainfalls: {highestRainfall}\nThis is the average of the rainfalls: {averageRainfall}")