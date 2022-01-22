def stringRepeater(string, repeatCount):
    addition = string
    for i in range(repeatCount - 1):
        string = string + addition
    return string

def main():

    string = str(input("Enter the string which you want to be repeated: "))
    repeatCount = int(input("How many times shall this string be repeated? "))
    repeatedString = stringRepeater(string, repeatCount)
    print(f"This is the repeated string: {repeatedString}")

if __name__ == "__main__":
    main()
