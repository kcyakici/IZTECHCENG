rows = int(input("Enter the number of rows for the reverse pyramid: "))

for i in range(rows):
    print("  " * i + "* " * ((rows * 2 - 1) - 2 * i))
    print()