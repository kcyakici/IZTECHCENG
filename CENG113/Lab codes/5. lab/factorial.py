number = int(input("Enter the integer of which you wish you take factorial: "))
factorial = 1

if number == 1 or number == 0:
    result = 1
    print("The factorial of",number,"is",result)
elif number < 0:
    print("Only non-negative numbers can be factored.")
elif number > 1: 
    for i in range(1 , number):
        factorial = factorial * (i+1)
        result = factorial
    print("The factorial of",number,"is",result)
