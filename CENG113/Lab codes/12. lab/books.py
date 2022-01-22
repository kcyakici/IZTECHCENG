def constructDict(bookList):
    for book in bookList:
        titleLenght = len(book)
        titleCharacters = len(set(book))
        bookDictionary = {book : (titleLenght, titleCharacters)}
    return bookDictionary

def printDict(dictionary):
    for d in dictionary:
        print (f"{d} -> dictionary[{d}] ")

def updateDict(dictionary):
    for bd in dictionary:
        avg = (dictionary[bd][0] + dictionary[bd][1]) / 2
        dictionary[bd] = (dictionary[bd][0], dictionary[bd][1], avg)

def main():
    books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
    bookDict = constructDict(books)
    printDict(bookDict)
    updateDict(bookDict)
    printDict(bookDict)

if __name__ == "__main__":
    main()
