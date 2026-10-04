import time
import math
def recursive_binary_search(lst, target):
    if not lst:
        return False
    midpoint = len(lst)
    if lst[midpoint] == target:
        return True
    elif lst[midpoint] < target:
        return recursive_binary_search(lst[midpoint + 1:], target)
    else:
        return recursive_binary_search(lst[:midpoint], target)
def binary_search(lst, target):
    first = 0
    last = len(lst) - 1
    while first <= last:
        midpoint = (first + last)
        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
def linear_search(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return i
    return None
def log_performance():
    for i in range(10, 19):
        size = int(math.pow(10, i))
        numbers = list(range(size))
        target = size - 3
        print(f"\n-> Quantity: {size} (10 to the power of {i})")
        print("Linear search: skipped")
        binary_search_time = measure_time(binary_search, numbers, target)
        print(f"Binary search: {binary_search_time:.6f} seconds")
        recursive_search_time = measure_time(recursive_binary_search, numbers, target)
        print(f"Recursive binary search: {recursive_search_time:.6f} seconds")
        write_to_file(size, binary_search_time, recursive_search_time)
def measure_time(search_function, numbers, target):
    start_time = time.time()
    search_function(numbers, target)
    return time.time() - start_time
def write_to_file(size, binary_search_time, recursive_search_time):
    with open("data.csv", "a") as file:
        file.write(f"{size};null;{binary_search_time:.6f};{recursive_search_time:.6f}\n")
if __name__ == "__main__":
    log_performance()