def cluster(userList):

    
    userList.sort()

    clusterList = []
    cluster = []
    j = 0
    i = 0
    for i in range(len(userList)):

        minimum = userList[j] * 2
        maximum = userList[i]

        if minimum >= maximum:

            cluster.append(maximum)
        else:

            clusterList.append(cluster)
            cluster = [maximum]
            j = i

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
                # 10 4 1 2 3 9 5 43 85 (87) 17 8 58 113 47

                print("Please enter an integer or type 'n'!")
    
    cList = cluster(userList)
    print(f"{cList}")

if __name__ == "__main__":
    main()
