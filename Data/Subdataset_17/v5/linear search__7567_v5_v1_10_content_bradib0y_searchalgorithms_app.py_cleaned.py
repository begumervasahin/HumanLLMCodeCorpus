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
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None
def log_search_times(data, filename="data.csv"):
    with open(filename, "a") as file:
        file.write(";".join(map(str, data)) + "\n")
def test_search_algorithms():
    for exponent in range(10, 19):
        numbers = list(range(0, int(math.pow(10, exponent))))
        target = int(math.pow(10, exponent)) - 3
        print(f"\n-> Quantity: {len(numbers)} (10 to the power of {exponent})")
        print("Linear search: null")
        data = [len(numbers), "null"]
        start_time = time.time()
        binary_search_result = binary_search(numbers, target)
        binary_search_time = time.time() - start_time
        print(binary_search_result)
        print(f"Binary search: {binary_search_time:.5f} seconds")
        data.append(f"{binary_search_time:.5f}")
        start_time = time.time()
        recursive_binary_search_result = recursive_binary_search(numbers, target)
        recursive_binary_search_time = time.time() - start_time
        print(recursive_binary_search_result)
        print(f"Recursive binary search: {recursive_binary_search_time:.5f} seconds")
        data.append(f"{recursive_binary_search_time:.5f}")
        log_search_times(data)
if __name__ == "__main__":
    test_search_algorithms()