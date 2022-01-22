# boş bir dizelge yarat
# for ile dönerek verilen dizelgeyi gez
# şayet gezdiğin öge yarattığında yoksa ekle
# dizelgenin doldurulması bittiğinde bubble sort ya da başka bir yöntem kullan

def getUniqueList(list):
    uniqueList = []
    for element in list:
        if element not in uniqueList:
            uniqueList.append(element)
    return uniqueList

def getSortedList(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            swapped = False
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swapped = True
        if not swapped:
            return list
    return list


def main():
    L = [5, 2, 1, 1, 2, 4, 3, 5]

    uniqueList = getUniqueList(L)
    uniqueSortedList = getSortedList(uniqueList)

    print(f"This is the list before the operations: {L}")
    print(f"This is the list unique sorted list: {uniqueSortedList}")

main()