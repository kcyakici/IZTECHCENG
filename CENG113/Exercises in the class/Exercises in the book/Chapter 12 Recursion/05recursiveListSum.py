def getTotal(list):
    
    if len(list) == 1:
        return list[0]
    
    subTotal = getTotal(list[1:])
    return list[0] + subTotal
    
def main():
    L = [50,41,31,69,420,55,1,7]
    print(getTotal(L))

if __name__ == "__main__":
    main()
    print(50+41+31+69+420+55+1+7)

# 1 2 3 4 5

# 1 > getLargest(2,3,4,5)

# 4 5

# 4 > getLargest(5)