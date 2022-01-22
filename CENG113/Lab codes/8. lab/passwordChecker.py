def passwordChecker(password):
    for char in password:
        if char.isspace() or len(password) < 8:
            return 0
    noLetter = True
    noSpecial = True
    noDigit = True
    security = 0
    for char in password:
        if char.isalpha() and noLetter:
            security += 1
            noLetter = False
        elif char.isdigit() and noDigit:
            security += 1
            noDigit = False
        elif not char.isdigit() and not char.isalpha() and noSpecial:
            security += 1
            noSpecial = False
    return security

userPassword = input("Enter your password to check for security rating: ")

rating = passwordChecker(userPassword)

print(f"The security rating of your password is {rating} out of 3")