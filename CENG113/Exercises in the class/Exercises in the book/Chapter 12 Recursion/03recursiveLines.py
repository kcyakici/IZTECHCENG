def printAsterisk(rows):
    if rows == 0:
        return ""

    printAsterisk(rows-1)
    print(rows * "*")


def stringTriangle(rows):
    if rows == 0:
        return ""
    elif rows == 1:
        return "*"

    return printAsterisk(rows-1) + "\n" + (rows * "*")



def main():
    rows = int(input("Give a number: "))
    print(stringTriangle(rows))


if __name__ == "__main__":
    main()
