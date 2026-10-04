import time
import math
def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    midpoint = len(arr)
    if arr[midpoint] == target:
        return True
    elif arr[midpoint] < target:
        return recursive_binary_search(arr[midpoint + 1:], target)
    else:
        return recursive_binary_search(arr[:midpoint], target)
def binary_search(arr, target):
    first, last = 0, len(arr) - 1
    while first <= last:
        midpoint = (first + last)
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = range(0, int(math.pow(10, i)))
        target = int(math.pow(10, i)) - 3
        print(f"\n-> Quantity: {target + 3} (10 to the power of {i})")
        print("Linear search: null")
        start_time = time.time()
        binary_result = binary_search(numbers, target)
        binary_time = time.time() - start_time
        print(f"Binary search: {binary_result}")
        print(f"Time taken for Binary search: {binary_time:.6f} seconds")
        start_time = time.time()
        recursive_binary_result = recursive_binary_search(numbers, target)
        recursive_binary_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_binary_result}")
        print(f"Time taken for Recursive binary search: {recursive_binary_time:.6f} seconds")
        with open("data.csv", "a") as file:
            file.write(f"{len(numbers)};null;{binary_time:.6f};{recursive_binary_time:.6f}\n")
test_log()