import time
import math
def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
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
    for i, value in enumerate(lst):
        if value == target:
            return i
    return None
def test_search_algorithms():
    for i in range(10, 19):
        numbers = list(range(0, int(math.pow(10, i))))
        target = int(math.pow(10, i)) - 3
        print(f"\n-> Quantity: {len(numbers)} (10 to the power of {i})")
        print("Linear search: null")
        data = [len(numbers), "null"]
        start_time = time.time()
        print(binary_search(numbers, target))
        elapsed_time = time.time() - start_time
        print(f"Binary search: {elapsed_time:.5f} seconds")
        data.append(f"{elapsed_time:.5f}")
        start_time = time.time()
        print(recursive_binary_search(numbers, target))
        elapsed_time = time.time() - start_time
        print(f"Recursive binary search: {elapsed_time:.5f} seconds")
        data.append(f"{elapsed_time:.5f}")
        with open("data.csv", "a") as file:
            file.write(";".join(map(str, data)) + "\n")
if __name__ == "__main__":
    test_search_algorithms()