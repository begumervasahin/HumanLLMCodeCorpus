import random
from time import time
random_numbers = random.sample(range(1_000_000), 100_000)
sorted_random_numbers = sorted(random_numbers)
target_number = random.choice(sorted_random_numbers)
elapsed_unsorted = []
elapsed_sorted = []
elapsed_smallest = []
elapsed_binary = []
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
def measure_time(search_function, data, target):
    start_time = time()
    search_function(data, target)
    end_time = time()
    return end_time - start_time
def measure_times():
    for size in range(10_000, 100_001, 10_000):
        elapsed_unsorted.append(measure_time(linear_search, random_numbers[:size], target_number))
        elapsed_sorted.append(measure_time(sorted_linear_search, sorted_random_numbers[:size], target_number))
        elapsed_smallest.append(measure_time(find_smallest, random_numbers[:size], None))
        elapsed_binary.append(measure_time(binary_search, sorted_random_numbers[:size], target_number))
def print_results(times, description):
    print(f"\n{description} times:")
    for elapsed_time in times:
        print(elapsed_time)
measure_times()
print_results(elapsed_unsorted, "Unsorted Linear Search")
print_results(elapsed_sorted, "Sorted Linear Search")
print_results(elapsed_smallest, "Finding Smallest Element")
print_results(elapsed_binary, "Binary Search")