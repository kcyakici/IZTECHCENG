userInput = int(input("How many words would you like to enter? "))

with open("08word.txt", "w") as f:
    # using .write()

    for i in range(userInput):
        word = input("Enter a word: ")
        f.write(word + " ")

    # using .writelines()

#     wordList = []
#     for i in range(userInput):
#         word = input("Enter a word: ")
#         wordList.append(word)
    
#     f.writelines(wordList)

with open("08word.txt", "r") as f:
    content = f.readlines()

print(content)
