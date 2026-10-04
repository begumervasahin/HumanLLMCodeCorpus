import random
from time import time
def linear_search(values, target):
    return target in values
def sorted_linear_search(values, target):
    for value in values:
        if value == target:
            return True
        elif value > target:
            return False
    return False
def find_smallest(values):
    return min(values)
def binary_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (high + low)
        if values[mid] == target:
            return True
        elif target < values[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
random_numbers = random.sample(range(1000000), 100000)
sorted_random_numbers = sorted(random_numbers)
target_number = random.choice(sorted_random_numbers)
elapsed_unsorted = []
elapsed_sorted = []
elapsed_smallest = []
elapsed_binary = []
for size in range(10000, 100001, 10000):
    subset_random_numbers = random_numbers[:size]
    subset_sorted_numbers = sorted_random_numbers[:size]
    start_time = time()
    linear_search(subset_random_numbers, target_number)
    end_time = time()
    elapsed_unsorted.append(end_time - start_time)
    start_time = time()
    sorted_linear_search(subset_sorted_numbers, target_number)
    end_time = time()
    elapsed_sorted.append(end_time - start_time)
    start_time = time()
    find_smallest(subset_random_numbers)
    end_time = time()
    elapsed_smallest.append(end_time - start_time)
    start_time = time()
    binary_search(subset_sorted_numbers, target_number)
    end_time = time()
    elapsed_binary.append(end_time - start_time)
def print_elapsed_times(title, times):
    print(f"\n{title}")
    for time_elapsed in times:
        print(time_elapsed)
print_elapsed_times("Unsorted Linear Search times", elapsed_unsorted)
print_elapsed_times("Sorted Linear Search times", elapsed_sorted)
print_elapsed_times("Finding Smallest Element times", elapsed_smallest)
print_elapsed_times("Binary Search times", elapsed_binary)