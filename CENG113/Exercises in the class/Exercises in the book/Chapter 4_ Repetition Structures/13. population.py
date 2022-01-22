startingNumber = int(input("Enter the starting number of the organisms: "))
avgDailyIncrease = float(input("Enter the average daily increase percentage: ")) / 100
numberOfDays = int(input("Enter the number of days within which the organisms will reproduce: "))

print("Day Approximate\tPopulation")
population = startingNumber
print(f"1\t\t{population}")
for day in range(2, numberOfDays + 1):
    population = population + (population * avgDailyIncrease)
    print(f"{day}\t\t{population}")
