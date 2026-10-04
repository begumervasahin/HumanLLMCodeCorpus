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
    for index, element in enumerate(lst):
        if element == target:
            return index
    return None
def log_search_results():
    for i in range(10, 19):
        numbers = list(range(int(math.pow(10, i))))
        target_number = int(math.pow(10, i)) - 3
        datastring = f"{len(numbers)};"
        print(f"\n-> Quantity: {target_number + 3} (10 to the power of {i})")
        print("Linear search: null")
        datastring += "null;"
        start_time = time.time()
        binary_search(numbers, target_number)
        binary_search_time = time.time() - start_time
        print(f"Binary search: {binary_search_time:.6f} seconds")
        datastring += f"{binary_search_time:.6f};"
        start_time = time.time()
        recursive_binary_search(numbers, target_number)
        recursive_binary_search_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_binary_search_time:.6f} seconds")
        datastring += f"{recursive_binary_search_time:.6f}"
        with open("data.csv", "a") as file:
            file.write(datastring + "\n")
if __name__ == "__main__":
    log_search_results()