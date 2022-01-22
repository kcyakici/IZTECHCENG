import random
random.seed(12)

def getRandomList():

    list = random.sample(range(0, 10), 5)
    return list

def getOverlap(list1, list2):
    
    overlap = []
    for object1 in list1:
        for object2 in list2:
            if object1 == object2:
                overlap.append(object2)
    return overlap


list1 = getRandomList()
list2 = getRandomList()

print(list1)
print(list2)
print(getOverlap(list1, list2))
