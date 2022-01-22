import math

# for x in range(0, 510, 25):
#     function = 2 * (x/100) * math.sin(x/100) * math.cos((x/100)*(x/100)*math.sqrt(2*x/100))
#     print("The value of the function when x=",x/100,"is:",function)

x = 0
while x < 5.1:
    function = 2 * x * math.sin(x) * math.cos(x*x*(2*x)**(1/2))
    print("The value of the function when x=",x,"is:",function)
    x = x + 0.25