print("This is the quadratic function: ax^2 + bx + c")

a = float(input("Enter the quadratic parameter a: "))
b = float(input("Enter the quadratic parameter b: "))
c = float(input("Enter the quadratic parameter c: "))

discriminant = b * b - 4 * a * c

if discriminant > 0:
    print("There are two real roots")
elif discriminant == 0:
    print("There is one real root")
elif discriminant < 0:
    print("There are two complex roots")