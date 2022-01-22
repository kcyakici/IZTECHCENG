def getReverseList(L):
    if len(L) == 0:
        return []
    else:
        return [L[-1]] + getReverseList(L[:-1])

def main():
    L = [1,2,3,4]
    reverseL = getReverseList(L)
    print(reverseL)

if __name__=="__main__":
    main()