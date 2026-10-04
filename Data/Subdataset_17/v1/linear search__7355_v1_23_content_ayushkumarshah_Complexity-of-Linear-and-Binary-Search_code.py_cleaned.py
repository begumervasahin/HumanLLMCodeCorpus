import random
from time import time
def linearSearch(theValues, target):
    for value in theValues:
        if value == target:
            return True
    return False
def sortedLinearSearch(theValues, target):
    for value in theValues:
        if value == target:
            return True
        elif value > target:
            return False
    return False
def findSmallest(theValues):
    smallest = theValues[0]
    for value in theValues[1:]:
        if value < smallest:
            smallest = value
    return smallest
def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low)
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
myrandomnumber = random.sample(range(1000000), 100000)
mysortedrandomnumber = sorted(myrandomnumber)
randomnumberfromthelist = random.choice(mysortedrandomnumber)
elapsed_unsorted = []
elapsed_sorted = []
elapsed_smallest = []
elapsed_binary = []
for i in range(10000, 100001, 10000):
    start_time = time()
    linearSearch(myrandomnumber[:i], randomnumberfromthelist)
    end_time = time()
    elapsed_unsorted.append(end_time - start_time)
    start_time = time()
    sortedLinearSearch(mysortedrandomnumber[:i], randomnumberfromthelist)
    end_time = time()
    elapsed_sorted.append(end_time - start_time)
    start_time = time()
    findSmallest(myrandomnumber[:i])
    end_time = time()
    elapsed_smallest.append(end_time - start_time)
    start_time = time()
    binarySearch(mysortedrandomnumber[:i], randomnumberfromthelist)
    end_time = time()
    elapsed_binary.append(end_time - start_time)
print("\nUnsorted Linear Search times")
for time_elapsed in elapsed_unsorted:
    print(time_elapsed)
print("\nSorted Linear Search times")
for time_elapsed in elapsed_sorted:
    print(time_elapsed)
print("\nFinding Smallest element times")
for time_elapsed in elapsed_smallest:
    print(time_elapsed)
print("\nBinary Search times")
for time_elapsed in elapsed_binary:
    print(time_elapsed)