def recursivePower(x, y):
    if y == 0:
        return 1
    else:
        return x * recursivePower(x, y-1)

def main():
    base = int(input("Give base: "))
    power = int(input("Give power: "))
    print(recursivePower(base,power))

if __name__ == "__main__":
    main()
