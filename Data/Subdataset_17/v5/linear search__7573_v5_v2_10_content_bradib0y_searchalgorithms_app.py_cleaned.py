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
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None
def test_log():
    for i in range(10, 19):
        numbers = list(range(0, int(math.pow(10, i))))
        target_number = int(math.pow(10, i)) - 3
        print(f"\n-> Quantity: {len(numbers)} (10^{i})")
        print("Linear search: null")
        start_time = time.time()
        binary_search(numbers, target_number)
        binary_time = time.time() - start_time
        print(f"Binary search: {binary_time:.6f} seconds")
        start_time = time.time()
        recursive_binary_search(numbers, target_number)
        recursive_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_time:.6f} seconds")
        with open("data.csv", "a") as file:
            data_string = f"{len(numbers)};null;{binary_time:.6f};{recursive_time:.6f}\n"
            file.write(data_string)
if __name__ == "__main__":
    test_log()