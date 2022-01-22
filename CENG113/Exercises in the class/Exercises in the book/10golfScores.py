with open("10golf.txt", "w") as f:
    inputsAreCorrect = False

    while not inputsAreCorrect:
        playerName = input("Enter the name of the player: ")

        if playerName.isalpha():

            try:
                score = int(input("Enter the score of the player: "))
                inputsAreCorrect = True

            except ValueError:
                print("Expected a number as the second input.")
        
        else:
            print("Expected a string input")

        if inputsAreCorrect:
            f.writelines(playerName + " " + str(score))
            f.writelines("\n")
            exit = input("Would you like to stop adding players? (y/n): ")
            if exit.lower() == "y":
                inputsAreCorrect = False
