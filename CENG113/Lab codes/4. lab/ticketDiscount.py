ticketCost = 3

userAge = int(input("Please enter your age: "))

if userAge >= 0 and (userAge < 6 or userAge > 60):
    print("Your ticket is for free")
elif userAge >= 6 and userAge < 18:
    print("Your ticket cost: " +  str(ticketCost * 0.5) + " TL")
elif userAge >= 18:
    print("Your ticket cost: " + str(ticketCost) + " TL")
else:
    print("Enter a valid age")