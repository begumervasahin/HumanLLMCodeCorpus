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
    low, high = 0, len(theValues) - 1
    while low <= high:
        mid = (high + low)
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
random.seed(42)
random_numbers = random.sample(range(1000000), 100000)
sorted_random_numbers = sorted(random_numbers)
target_number = random.choice(sorted_random_numbers)
elapsed_unsorted = []
elapsed_sorted = []
elapsed_smallest = []
elapsed_binary = []
for size in range(10000, 100001, 10000):
    start_time = time()
    linearSearch(random_numbers[:size], target_number)
    end_time = time()
    elapsed_unsorted.append(end_time - start_time)
print("\nUnsorted Linear Search times:")
for i in range(10):
    print(elapsed_unsorted[i])
for size in range(10000, 100001, 10000):
    start_time = time()
    sortedLinearSearch(sorted_random_numbers[:size], target_number)
    end_time = time()
    elapsed_sorted.append(end_time - start_time)
print("\nSorted Linear Search times:")
for i in range(10):
    print(elapsed_sorted[i])
for size in range(10000, 100001, 10000):
    start_time = time()
    findSmallest(random_numbers[:size])
    end_time = time()
    elapsed_smallest.append(end_time - start_time)
print("\nFinding Smallest element times:")
for i in range(10):
    print(elapsed_smallest[i])
for size in range(10000, 100001, 10000):
    start_time = time()
    binarySearch(sorted_random_numbers[:size], target_number)
    end_time = time()
    elapsed_binary.append(end_time - start_time)
print("\nBinary Search times:")
for i in range(10):
    print(elapsed_binary[i])