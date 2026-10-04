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
def measure_search_time(search_func, values, target):
    start_time = time()
    search_func(values, target)
    end_time = time()
    return end_time - start_time
elapsed_times = {
    "unsorted_linear_search": [],
    "sorted_linear_search": [],
    "find_smallest": [],
    "binary_search": []
}
for i in range(10000, 100001, 10000):
    elapsed_times["unsorted_linear_search"].append(measure_search_time(linear_search, random_numbers[:i], target_number))
    elapsed_times["sorted_linear_search"].append(measure_search_time(sorted_linear_search, sorted_random_numbers[:i], target_number))
    elapsed_times["find_smallest"].append(measure_search_time(find_smallest, random_numbers[:i], target_number))
    elapsed_times["binary_search"].append(measure_search_time(binary_search, sorted_random_numbers[:i], target_number))
def print_elapsed_times(title, times):
    print(f"\n{title} times:")
    for time_elapsed in times:
        print(time_elapsed)
print_elapsed_times("Unsorted Linear Search", elapsed_times["unsorted_linear_search"])
print_elapsed_times("Sorted Linear Search", elapsed_times["sorted_linear_search"])
print_elapsed_times("Finding Smallest Element", elapsed_times["find_smallest"])
print_elapsed_times("Binary Search", elapsed_times["binary_search"])