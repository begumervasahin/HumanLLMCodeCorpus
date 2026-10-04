import random
from time import time
def linearSearch(values, target):
    for value in values:
        if value == target:
            return True
    return False
def sortedLinearSearch(values, target):
    for value in values:
        if value == target:
            return True
        elif value > target:
            return False
    return False
def findSmallest(values):
    smallest = values[0]
    for value in values[1:]:
        if value < smallest:
            smallest = value
    return smallest
def binarySearch(values, target):
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
random.seed(42)
random_numbers = random.sample(range(1000000), 100000)
sorted_random_numbers = sorted(random_numbers)
target_number = random.choice(sorted_random_numbers)
elapsed_times = {
    'unsorted_linear': [],
    'sorted_linear': [],
    'find_smallest': [],
    'binary': []
}
def measure_time(func, data, target):
    start_time = time()
    func(data, target)
    end_time = time()
    return end_time - start_time
for size in range(10000, 100001, 10000):
    elapsed_times['unsorted_linear'].append(measure_time(linearSearch, random_numbers[:size], target_number))
    elapsed_times['sorted_linear'].append(measure_time(sortedLinearSearch, sorted_random_numbers[:size], target_number))
    elapsed_times['find_smallest'].append(measure_time(findSmallest, random_numbers[:size], target_number))
    elapsed_times['binary'].append(measure_time(binarySearch, sorted_random_numbers[:size], target_number))
def print_times(method_name, times):
    print(f"\n{method_name} times:")
    for time in times:
        print(time)
print_times('Unsorted Linear Search', elapsed_times['unsorted_linear'])
print_times('Sorted Linear Search', elapsed_times['sorted_linear'])
print_times('Finding Smallest Element', elapsed_times['find_smallest'])
print_times('Binary Search', elapsed_times['binary'])