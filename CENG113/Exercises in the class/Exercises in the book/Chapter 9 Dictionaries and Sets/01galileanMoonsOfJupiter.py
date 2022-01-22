moonRadii = {"Io": 1821.6, "Europa": 1560.8, "Ganymede": 2634.1, "Callisto": 2410.3}
moonGravities = {"Io": 1.796, "Europa": 1.314, "Ganymede": 1.428, "Callisto": 1.235}
moonPeriods = {"Io": 1.769, "Europa": 3.551, "Ganymede": 7.154, "Callisto": 16.689}

print(f"Moons of Jupiter: ")
for moon in moonRadii:
    print(f"{moon}")

userInput = input("Enter a name of a moon to receive additional information: ")
if userInput in moonRadii:
    moon = userInput
    radiusInformation = moonRadii[userInput]
    gravityInformation = moonGravities[userInput]
    periodInformation = moonPeriods[userInput]

    print(f"Radius of the {moon}: {radiusInformation}\nGravity of the {moon}: {gravityInformation}\nPeriod of the {moon}: {radiusInformation}")
else:
    print("There is no such moon, try again.")