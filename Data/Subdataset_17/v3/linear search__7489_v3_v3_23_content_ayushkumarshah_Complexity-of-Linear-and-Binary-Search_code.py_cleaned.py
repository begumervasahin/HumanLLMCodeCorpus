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
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high)
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
def measure_time_and_print(func, func_name, numbers, target):
    elapsed_times = []
    for size in range(10000, 100001, 10000):
        start_time = time()
        func(numbers[:size], target)
        end_time = time()
        elapsed_times.append(end_time - start_time)
    print(f"\n{func_name} times:")
    for i, elapsed_time in enumerate(elapsed_times):
        print(f"Size {10000 * (i + 1)}: {elapsed_time:.6f} seconds")
measure_time_and_print(linear_search, "Unsorted Linear Search", random_numbers, target_number)
measure_time_and_print(sorted_linear_search, "Sorted Linear Search", sorted_random_numbers, target_number)
measure_time_and_print(find_smallest, "Finding Smallest Element", random_numbers, target_number)
measure_time_and_print(binary_search, "Binary Search", sorted_random_numbers, target_number)