list1 = [2, 4]
list2 = [1, 2, 3, 5, 6, 8, 9]
list3 = []
list4 = []

for element1 in list1:
    list4.append(element1)
    for element2 in list2:
        if element1 == element2:
            list3.append(element2)
            break
    if list3 != list4:
        print("The first list is not a sublist of the second list")
        break

if list4 == list3:
    print ("The first list is a sublist of the second list")


# the one above is more efficient

# for element1 in list1: 
#     for element2 in list2:
#         if element1 == element2:
#             list3.append(element2)
# if list1 == list3:
#     print ("The first list is a sublist of the second list")
# else:
#     print("The first list is not a sublist of the second list")
