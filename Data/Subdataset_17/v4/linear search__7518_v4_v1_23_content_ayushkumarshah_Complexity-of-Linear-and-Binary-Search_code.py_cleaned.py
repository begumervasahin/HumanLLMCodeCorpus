import random
from time import time
def linear_search(values, target):
    for value in values:
        if value == target:
            return True
    return False
def sorted_linear_search(values, target):
    for value in values:
        if value == target:
            return True
        elif value > target:
            return False
    return False
def find_smallest(values):
    smallest = values[0]
    for value in values[1:]:
        if value < smallest:
            smallest = value
    return smallest
def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (high + low)
        if values[mid] == target:
            return True
        elif target < values[mid]:
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
for i in range(10000, 100001, 10000):
    start_time = time()
    linear_search(random_numbers[:i], target_number)
    end_time = time()
    elapsed_unsorted.append(end_time - start_time)
print("\nUnsorted Linear Search times:")
for time_elapsed in elapsed_unsorted:
    print(time_elapsed)
for i in range(10000, 100001, 10000):
    start_time = time()
    sorted_linear_search(sorted_random_numbers[:i], target_number)
    end_time = time()
    elapsed_sorted.append(end_time - start_time)
print("\nSorted Linear Search times:")
for time_elapsed in elapsed_sorted:
    print(time_elapsed)
for i in range(10000, 100001, 10000):
    start_time = time()
    find_smallest(random_numbers[:i])
    end_time = time()
    elapsed_smallest.append(end_time - start_time)
print("\nFinding Smallest Element times:")
for time_elapsed in elapsed_smallest:
    print(time_elapsed)
for i in range(10000, 100001, 10000):
    start_time = time()
    binary_search(sorted_random_numbers[:i], target_number)
    end_time = time()
    elapsed_binary.append(end_time - start_time)
print("\nBinary Search times:")
for time_elapsed in elapsed_binary:
    print(time_elapsed)