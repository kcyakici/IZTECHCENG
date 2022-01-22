def cluster(userList):

    
    userList.sort()

    clusterList = []
    j = -1
    for i in range(len(userList)):

        if i < j:
            continue

        cluster = []
        cluster.append(userList[i])

        for j in range(i + 1, len(userList)):

            if userList[i]*2 >= userList[j]:

                cluster.append(userList[j])

            elif userList[i]*2 <= userList[j]:

                break

        clusterList.append(cluster)

    return clusterList

def main():

    
    userInput = "zxcvbnm123"
    userList = []

    while userInput != "n":

        userInput = input("Integer to add to the list: ")

        if userInput != "n":

            try:

                userInput = int(userInput)
                userList.append(userInput)
                print(f"Current list: {userList}")

            except ValueError:

                print("Please enter an integer or type 'n'!")
    
    cList = cluster(userList)
    print(f"{cList}")

if __name__ == "__main__":
    main()
