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
    first = 0
    last = len(arr) - 1
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
    for i in range(10, 19):
        numbers = range(0, int(math.pow(10, i)))
        target_number = int(math.pow(10, i)) - 3
        data_string = f"{len(numbers)};"
        print(f"\n-> Quantity: {len(numbers)} (10 to the power of {i})")
        print("Linear search: null")
        data_string += "null;"
        start_time = time.time()
        binary_search(numbers, target_number)
        binary_search_time = time.time() - start_time
        print(f"Binary search: {binary_search_time}")
        data_string += f"{binary_search_time};"
        start_time = time.time()
        recursive_binary_search(numbers, target_number)
        recursive_binary_search_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_binary_search_time}")
        data_string += f"{recursive_binary_search_time}"
        with open("data.csv", "a") as file:
            file.write(data_string + "\n")
if __name__ == "__main__":
    test_log()