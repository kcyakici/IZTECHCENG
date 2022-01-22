import random as rd

lotteryNumber = []

for i in range(7):
    randomNumber = rd.randint(0,9)
    lotteryNumber.append(randomNumber)

print(f"This is the lottery number: ")

for number in lotteryNumber:
    print(number, end=" ")
