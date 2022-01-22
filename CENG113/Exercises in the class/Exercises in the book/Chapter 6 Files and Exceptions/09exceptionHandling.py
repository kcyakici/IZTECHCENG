import sys

try:
    f = open("06numbers.txt", "r")
    content = f.readlines()
    
    summation = 0
    count = 0

    for line in content:
        line = line.split()

        for number in line:
            try:
                number = int(number)
                summation = summation + number
                count += 1

            except ValueError:
                print("There seems to be a nonnumerical element in the file. Process has been stopped.")
                sys.exit(1)

    print(summation / count)

    f.close()

except IOError:
    print("There seems to be no such file")
