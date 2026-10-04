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
    first, last = 0, len(lst) - 1
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
    for i, value in enumerate(lst):
        if value == target:
            return i
    return None
def measure_search_time(search_func, lst, target):
    start_time = time.time()
    search_func(lst, target)
    return time.time() - start_time
def log_search_performance(size, binary_search_time, recursive_search_time):
    with open("data.csv", "a") as file:
        file.write(f"{size};null;{binary_search_time:.6f};{recursive_search_time:.6f}\n")
def test_log():
    for i in range(10, 19):
        size = int(math.pow(10, i))
        numbers = list(range(size))
        target = size - 3
        print(f"\n-> Quantity: {size} (10^{i})")
        print("Linear search: null")
        binary_search_time = measure_search_time(binary_search, numbers, target)
        print(f"Binary search: {binary_search_time:.6f} seconds")
        recursive_search_time = measure_search_time(recursive_binary_search, numbers, target)
        print(f"Recursive binary search: {recursive_search_time:.6f} seconds")
        log_search_performance(size, binary_search_time, recursive_search_time)
if __name__ == "__main__":
    test_log()