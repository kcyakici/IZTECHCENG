totalBugs = 0

for day in range(5):
    bugCollected = int(input("Bugs collected today: "))
    totalBugs = totalBugs + bugCollected

print(f"The total number of bugs collected: {totalBugs}")