def kilometerCalculator(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():

    kilometers = float(input("Enter the kilometers to convert into miles: "))
    miles = kilometerCalculator(kilometers)
    print(f"{kilometers} KM is {miles} miles.")

if __name__ == "__main__":
    main()
    