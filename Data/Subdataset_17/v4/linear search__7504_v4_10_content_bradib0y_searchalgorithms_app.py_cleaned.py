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
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = list(range(int(math.pow(10, i))))
        number = int(math.pow(10, i)) - 3
        data_string = f"{len(numbers)};"
        print(f"\n-> Quantity: {number + 3} (10 to the power of {i})")
        print("Linear search: null")
        data_string += "null;"
        start_time = time.time()
        binary_search(numbers, number)
        binary_search_time = time.time() - start_time
        print(f"Binary search: {binary_search_time}")
        data_string += f"{binary_search_time};"
        start_time = time.time()
        recursive_binary_search(numbers, number)
        recursive_binary_search_time = time.time() - start_time
        print(f"Recursive binary search: {recursive_binary_search_time}")
        data_string += f"{recursive_binary_search_time}"
        with open("data.csv", "a") as file:
            file.write(data_string + "\n")
if __name__ == "__main__":
    test_log()