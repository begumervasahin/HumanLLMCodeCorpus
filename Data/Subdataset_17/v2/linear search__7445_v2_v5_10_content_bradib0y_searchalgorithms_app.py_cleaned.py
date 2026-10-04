import time
import math
def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
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
    for i, num in enumerate(arr):
        if num == target:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = list(range(0, int(math.pow(10, i))))
        target = int(math.pow(10, i)) - 3
        data_string = f"{len(numbers)};"
        print(f"\n-> Quantity: {len(numbers)} (10 to the power of {i})")
        print("Linear search: null")
        data_string += "null;"
        start_time = time.time()
        print("Binary search result:", binary_search(numbers, target))
        binary_search_time = time.time() - start_time
        print("Time taken for Binary search:", binary_search_time)
        data_string += f"{binary_search_time};"
        start_time = time.time()
        print("Recursive binary search result:", recursive_binary_search(numbers, target))
        recursive_search_time = time.time() - start_time
        print("Time taken for Recursive binary search:", recursive_search_time)
        data_string += f"{recursive_search_time}"
        with open("data.csv", "a") as file:
            file.write(data_string + "\n")
if __name__ == "__main__":
    test_log()