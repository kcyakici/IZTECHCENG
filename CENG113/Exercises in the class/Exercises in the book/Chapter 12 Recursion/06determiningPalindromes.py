def palindrome(string):
    if len(string) == 0:
        return True
    elif len(string) == 1:
        return True
    else:
        return string[0] == string[-1] and palindrome(string[1:-2])

def main():
    userString = input("Give word: ")
    print(palindrome(userString))

if __name__ == "__main__":
    main()
