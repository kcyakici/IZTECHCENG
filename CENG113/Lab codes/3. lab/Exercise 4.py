firstCarSpeed = float(input("Please enter the speed of the first car in km/h: "))
secondCarSpeed = float(input("Please enter the speed of the second car in km/h: "))
initialDistanceBetweenCars = float(input("Please enter the initial distance between the cars in kilometer: "))
finalDistanceBetweenCars = float(input("Please enter the final distance between the cars in kilometer: "))

hoursUntilFinalDistance = str((initialDistanceBetweenCars - finalDistanceBetweenCars) / (firstCarSpeed + secondCarSpeed))

hoursToMinute = float(hoursUntilFinalDistance) * 60

print("After " + str(hoursToMinute) + " minutes(s), the distance between the cars will be " + str(finalDistanceBetweenCars) + " kilometer(s).")