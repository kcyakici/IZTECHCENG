def multiplication(x, y):
    if y == 0 or x == 0:
        return 0
    elif y < 0 and x < 0:
        x, y = -x, -y
    elif y < 0:
        x, y = y, x

    return x + multiplication(x, y-1)

def main():
    x = int(input("Give a number: "))
    y = int(input("Give a number: "))
    result = multiplication(x, y)
    print(result)

if __name__ == "__main__":
    main()
