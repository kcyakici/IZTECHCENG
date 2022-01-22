def automobileCosts(loan, insurance, gas, oil, tires, maintenance):
    
    monthlyCost = loan + insurance + gas + oil + tires + maintenance
    return monthlyCost

def main():

    loanPayment = float(input("Enter the loan payment cost for your vehicle: "))
    insurance = float(input("Enter the insurace cost for your vehicle: "))
    gas = float(input("Enter the gas cost for your vehicle: "))
    oil = float(input("Enter the oil cost for your vehicle: "))
    tires = float(input("Enter the tire costs for your vehicle: "))
    maintenance = float(input("Enter the maintenance cost for your vehicle: "))

    monthly = automobileCosts(loanPayment, insurance, gas, oil, tires, maintenance)
    yearly = monthly * 12

    print(f"This is the monthly cost of your car: {monthly}\nThis is the yearly cost of your car: {yearly}")

if __name__ == "__main__":
    main()