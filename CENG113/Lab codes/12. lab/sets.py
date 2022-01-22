def uniqueList(list):
    uniqueList = set(list)
    return uniqueList

def intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection

def union(set1, set2):
    union = set1.union(set2)
    return union

def main():
    numbers1 = [2,3,4,20,5,5,15]
    numbers2 = [10,20,20,15,30,40]

    unique1 = uniqueList(numbers1)
    unique2 = uniqueList(numbers2)
    intersectList = intersection(unique1, unique2)
    uniList = union(unique1, unique2)
    print(intersectList, uniList)

if __name__ == "__main__":
    main()