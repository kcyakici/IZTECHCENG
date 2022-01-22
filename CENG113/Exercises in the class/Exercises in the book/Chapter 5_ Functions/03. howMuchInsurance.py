def insuranceMoney(replacementCost):
    insuranceMoney = replacementCost * 0.8
    return insuranceMoney

def main():
    
    replacementCost = float(input("Enter the replacement cost of your building: "))
    insurance = insuranceMoney(replacementCost)
    print(f"This is the minimum amount of insurance you should buy for the property: {insurance}")

if __name__ == "__main__":
    main()