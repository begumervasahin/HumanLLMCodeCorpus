import time
import math
def recursive_binary_search(lst, target):
    if not lst:
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
    for i, num in enumerate(lst):
        if num == target:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = range(0, int(math.pow(10, i)))
        number = int(math.pow(10, i)) - 3
        print(f"\n-> Quantity: {number + 3} (10 to the power of {i})")
        print("Linear search: null")
        log_start = time.time()
        binary_result = binary_search(numbers, number)
        binary_time = time.time() - log_start
        print(f"Binary search: {binary_time}")
        log_start = time.time()
        recursive_result = recursive_binary_search(numbers, number)
        recursive_time = time.time() - log_start
        print(f"Recursive binary search: {recursive_time}")
        with open("data.csv", "a") as file:
            data_string = f"{len(numbers)};null;{binary_time};{recursive_time}\n"
            file.write(data_string)
if __name__ == "__main__":
    test_log()