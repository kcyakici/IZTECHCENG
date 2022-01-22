from typing import Sequence


def gallonsOfPaint(sqrFeet):

    numberOfGallons = sqrFeet / 112
    return numberOfGallons

def hoursOfLabor(sqrFeet):

    hours = sqrFeet / 112 * 8
    return hours

def paintCost(gallons, gallonPrice):

    cost = gallons * gallonPrice
    return cost

def laborCharge(hours):

    labor = hours * 35
    return labor



def main():

    squareFoot = float(input("Enter the square feet which is to be painted: "))
    pricePerGallon = float(input("Enter the price per gallon of paint: "))
    
    hours = hoursOfLabor(squareFoot)
    gallons = gallonsOfPaint(squareFoot)
    costOfPaint = paintCost(gallons, pricePerGallon)
    labor = laborCharge(hours)
    total = labor + costOfPaint

    print(f"The number of gallons of paint required: {gallons}\nThehours of labor required: {hours}\nThe cost of the paint: {costOfPaint}\nThe labor charges: {labor}\nThe total cost of the paint job: {total}")

if __name__ == "__main__":
    main()