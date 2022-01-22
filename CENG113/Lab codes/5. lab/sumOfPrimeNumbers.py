M = [[7, 60, 43], [55, 25, 2]]

sumOfPrimes = 0
for row in M:
    for column in row:
        if column>1:
            for k in range(2, int(column**(1/2) + 1)):
                if(column%k)==0:
                    break
            else:
                sumOfPrimes = sumOfPrimes + column
                print(column, end=" ")
print("\nThis is the sum of the prime numbers in the list:",sumOfPrimes)
