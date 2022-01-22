def costClassA(count):

    price = count * 20
    return price

def costClassB(count):

    price = count * 15
    return price

def costClassC(count):

    price = count * 10
    return price


def main():

    aCount = int(input("Enter the number of Class A seats: "))
    bCount = int(input("Enter the number of Class B seats: "))
    cCount = int(input("Enter the number of Class A seats: "))
    
    price = costClassA(aCount) + costClassB(bCount) + costClassC(cCount)

    
    print(f"This is the total price for the seats: {price}")


if __name__ == "__main__":
    main()