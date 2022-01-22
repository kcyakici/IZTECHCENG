import random as rd

def roll(numberOfThrows):
    throwList = []

    for i in range(numberOfThrows):
        die = rd.randint(1, 6)
        throwList.append(die)
    
    throwList.sort()
    return throwList

def main():

    numberOfThrows = int(input("Enter a positive integer: "))
    
    throwList = roll(numberOfThrows)

    print(f"This is the die scores: {throwList}")

if __name__ == "__main__":
    main()