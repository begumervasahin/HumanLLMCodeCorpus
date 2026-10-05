import time
def linearSearch(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position += 1
    return found
def calcRuntime(search_function, myItem, myList):
    start = time.perf_counter()
    result = search_function(myItem, myList)
    end = time.perf_counter()
    elapsed = (end - start) * 100000
    return elapsed
if __name__ == "__main__":
    nums1 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    numToFind = int(input("What number do you want to find? "))
    isitFound = linearSearch(numToFind, nums1)
    timetoFind = calcRuntime(linearSearch, numToFind, nums1)
    if isitFound:
        print("Your item is in the list")
        print("Time to find: ", timetoFind)
    else:
        print("Your item is not in the list")
        print("Time to find: ", timetoFind)