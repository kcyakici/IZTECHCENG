def listPrimes(userInput):
    if userInput < 2:
        print("There are no prime numbers lesser than 2")
        return

    else:
        primeList = [2]
        for i in range(userInput):
            if i > 1 and i%2 != 0:
                for k in range(2, int(i**(1/2) + 1)):
                    if(i%k)==0:
                        break

                else:
                    primeList.append(i)
        return primeList

def computeSum(list):
    total = 0
    for number in list:
        total = total + number
    return total
                    


userInput = int(input("Enter a number to add together all the prime numbers which are lesser than given number: "))

listOfPrimes = listPrimes(userInput)
sumOfPrimes = computeSum(listOfPrimes)

print(f"The list of prime numbers lesser than the number you have entered:\n{listOfPrimes}")
print(f"This is the sum of the prime numbers in the list:\n{sumOfPrimes}")