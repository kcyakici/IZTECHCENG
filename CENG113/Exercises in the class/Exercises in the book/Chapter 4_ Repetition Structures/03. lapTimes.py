lapCount = int(input("Enter the lap count: "))

fastestLap = 999999999
slowestLap = 0
totalTime = 0

for lap in range(lapCount):
    lapTime = int(input("Enter the lap time in seconds: "))
    totalTime = totalTime + lapTime
    if lapTime > slowestLap:
        slowestLap = lapTime
    if lapTime < fastestLap:
        fastestLap = lapTime

averageTime = totalTime / lapCount

print(fastestLap, slowestLap, averageTime)




