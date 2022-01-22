days = int(input("Enter the number of days: "))
pennies = 0.5

for day in range(1, days+1):
    pennies = (pennies)*2
    print(f"Your salary in dollars on day {day}: {pennies/100}")