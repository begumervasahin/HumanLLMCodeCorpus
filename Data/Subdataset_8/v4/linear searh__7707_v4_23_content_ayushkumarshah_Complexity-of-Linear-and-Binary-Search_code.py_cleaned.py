import random
from time import time
my_random_numbers = random.sample(range(1000000), 100000)
my_sorted_random_numbers = sorted(my_random_numbers)
random_number_from_the_list = random.choice(my_sorted_random_numbers)
elapsed_unsorted = []
elapsed_sorted = []
elapsed_smallest = []
elapsed_binary = []
def linear_search(the_values, target):
    for value in the_values:
        if value == target:
            return True
    return False
def sorted_linear_search(the_values, target):
    for value in the_values:
        if value == target:
            return True
        elif value > target:
            return False
    return False
def find_smallest(the_values):
    smallest = the_values[0]
    for value in the_values[1:]:
        if value < smallest:
            smallest = value
    return smallest
def binary_search(the_values, target):
    low = 0
    high = len(the_values) - 1
    while low <= high:
        mid = (high + low)
        if the_values[mid] == target:
            return True
        elif target < the_values[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
for i in range(10000, 100001, 10000):
    start_time = time()
    linear_search(my_random_numbers[:i], random_number_from_the_list)
    end_time = time()
    elapsed_unsorted.append(end_time - start_time)
print("\nUnsorted Linear Search times:")
for time_val in elapsed_unsorted:
    print(time_val)
for i in range(10000, 100001, 10000):
    start_time = time()
    sorted_linear_search(my_sorted_random_numbers[:i], random_number_from_the_list)
    end_time = time()
    elapsed_sorted.append(end_time - start_time)
print("\nSorted Linear Search times:")
for time_val in elapsed_sorted:
    print(time_val)
for i in range(10000, 100001, 10000):
    start_time = time()
    find_smallest(my_random_numbers[:i])
    end_time = time()
    elapsed_smallest.append(end_time - start_time)
print("\nFinding Smallest Element times:")
for time_val in elapsed_smallest:
    print(time_val)
for i in range(10000, 100001, 10000):
    start_time = time()
    binary_search(my_sorted_random_numbers[:i], random_number_from_the_list)
    end_time = time()
    elapsed_binary.append(end_time - start_time)
print("\nBinary Search times:")
for time_val in elapsed_binary:
    print(time_val)