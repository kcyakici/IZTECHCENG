def printing(n):
    print(n)
    if n >= 2:
        printing(n-2)

def main():
    userInput = int(input("Give a number: "))
    printing(userInput)

if __name__ == "__main__":
    main()
