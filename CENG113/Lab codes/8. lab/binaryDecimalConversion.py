def binaryToDec(binary):
    decimal = int(binary, 2)
    return decimal

def decToBinary(decimal):
    binary = bin(decimal)
    binary = binary[2:]
    return binary

binary = decToBinary(18)
decimal = binaryToDec("10010")

print(decimal,binary)