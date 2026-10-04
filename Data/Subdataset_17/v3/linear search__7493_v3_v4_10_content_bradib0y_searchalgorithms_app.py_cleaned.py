import time
import math
def recursive_binary_search(arr, target):
    if not arr:
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
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None
def test_log():
    with open("data.csv", "a") as file:
        for exponent in range(1, 8):
            numbers = list(range(0, int(math.pow(10, exponent))))
            target = int(math.pow(10, exponent)) - 3
            data_string = f"{len(numbers)};"
            print(f"\n-> Quantity: {target + 3} (10 to the power of {exponent})")
            print("Linear search: null")
            data_string += "null;"
            start_time = time.time()
            binary_search(numbers, target)
            elapsed_time = time.time() - start_time
            print(f"Binary search: {elapsed_time}")
            data_string += f"{elapsed_time};"
            start_time = time.time()
            recursive_binary_search(numbers, target)
            elapsed_time = time.time() - start_time
            print(f"Recursive binary search: {elapsed_time}")
            data_string += f"{elapsed_time}"
            file.write(data_string + "\n")
test_log()