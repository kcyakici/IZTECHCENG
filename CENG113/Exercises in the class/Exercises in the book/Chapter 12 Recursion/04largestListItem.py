def getLargest(list):
    
    if len(list) == 1:
        return list[0]
    
    subLargest = getLargest(list[1:])
    return list[0] if list[0] > subLargest else subLargest
    
def main():
    L = [50,41,31,69,420,55,1,7]
    print(getLargest(L))

if __name__ == "__main__":
    main()

# 1 2 3 4 5

# 1 > getLargest(2,3,4,5)

# 4 5

# 4 > getLargest(5)