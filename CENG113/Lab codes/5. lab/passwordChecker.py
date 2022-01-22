password = "abc123"

passwordIsIncorrect = True

while passwordIsIncorrect:
    userPassword = input("Enter password: ")
    if userPassword == password:
        print("Welcome")
        passwordIsIncorrect = False
    elif userPassword == "help":
        passwordList = list(password)
        print("The first character of your password is",passwordList[0])
    else:
        print("Wrong password")