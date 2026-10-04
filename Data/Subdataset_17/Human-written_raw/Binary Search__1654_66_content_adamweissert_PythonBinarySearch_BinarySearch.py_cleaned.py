import time
def binarySearch(nums, item):
    first = 0
    last = len(nums)-1
    found = False
    start = time.time()
    while first <= last and not found:
        middle = (first + last)
        if nums[middle] == item:
            found = True;
        else:
            if item < nums[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found
def calcRuntime(binarySearch, nums, item):
    start = time.perf_counter()
    result = binarySearch(nums, item)
    end = time.perf_counter()
    elapsed = (end - start) * 100000
    return elapsed
if(__name__ == "__main__"):
    list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    numToFind = int(input("What number do you want to find? "))
    isitFound = binarySearch(list, numToFind)
    timetoFind = calcRuntime(binarySearch, list, numToFind)
    if(isitFound):
        print("Your item is in the list")
        print("Time to find: ", timetoFind)
    else:
        print("Your item is not in the list")
        print("Time spent searching: ", timetoFind)