import random
from time import time
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
    low, high = 0, len(the_values) - 1
    while low <= high:
        mid = (high + low)
        if the_values[mid] == target:
            return True
        elif target < the_values[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
def measure_time_and_print(func, func_name, numbers, target):
    elapsed_times = []
    for size in range(10000, 100001, 10000):
        start_time = time()
        func(numbers[:size], target)
        end_time = time()
        elapsed_times.append(end_time - start_time)
    print(f"\n{func_name} times:")
    for i, elapsed in enumerate(elapsed_times, start=1):
        print(f"Run {i}: {elapsed:.6f} seconds")
def main():
    random.seed(42)
    random_numbers = random.sample(range(1000000), 100000)
    sorted_random_numbers = sorted(random_numbers)
    target_number = random.choice(sorted_random_numbers)
    measure_time_and_print(linear_search, "Unsorted Linear Search", random_numbers, target_number)
    measure_time_and_print(sorted_linear_search, "Sorted Linear Search", sorted_random_numbers, target_number)
    measure_time_and_print(find_smallest, "Finding Smallest Element", random_numbers, target_number)
    measure_time_and_print(binary_search, "Binary Search", sorted_random_numbers, target_number)
if __name__ == "__main__":
    main()