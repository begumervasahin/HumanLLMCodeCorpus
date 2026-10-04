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
        num_elements = int(math.pow(10, i))
        numbers = list(range(num_elements))
        target = num_elements - 3
        print(f"\n-> Quantity: {num_elements} (10 to the power of {i})")
        linear_search_time = "null"
        print("Linear search: null")
        start_time = time.time()
        binary_search_result = binary_search(numbers, target)
        binary_search_time = time.time() - start_time
        print(f"Binary search result: {binary_search_result}")
        print(f"Time taken for Binary search: {binary_search_time}")
        start_time = time.time()
        recursive_binary_search_result = recursive_binary_search(numbers, target)
        recursive_binary_search_time = time.time() - start_time
        print(f"Recursive binary search result: {recursive_binary_search_result}")
        print(f"Time taken for Recursive binary search: {recursive_binary_search_time}")
        data_string = f"{num_elements};{linear_search_time};{binary_search_time};{recursive_binary_search_time}"
        with open("data.csv", "a") as file:
            file.write(data_string + "\n")
if __name__ == "__main__":
    test_log()