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
def test_log():
    for i in range(10, 19):
        size = int(math.pow(10, i))
        numbers = list(range(size))
        target = size - 3
        print(f"\n-> Quantity: {size} (10^{i})")
        print("Linear search: null")
        start_time = time.time()
        binary_search(numbers, target)
        binary_search_time = time.time() - start_time
        print(f"Binary search: {binary_search_time:.6f} seconds")
        start_time = time.time()
        recursive_binary_search(numbers, target)
        recursive_search_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_search_time:.6f} seconds")
        with open("data.csv", "a") as file:
            file.write(f"{size};null;{binary_search_time:.6f};{recursive_search_time:.6f}\n")
if __name__ == "__main__":
    test_log()