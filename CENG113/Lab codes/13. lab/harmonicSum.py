def harmonicSum(x):
    if x < 2:
        return 1
    else:
        return 1/x + harmonicSum(x-1)


def main():
    userInput = int(input("Enter a number: "))
    harmonic = harmonicSum(userInput)
    print(harmonic)

if __name__=="__main__":
    main()