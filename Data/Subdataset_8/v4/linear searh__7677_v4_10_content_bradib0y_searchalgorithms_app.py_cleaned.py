import time
import math
def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr)
        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
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
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = range(0, int(math.pow(10, i)))
        number = (int(math.pow(10, i)) - 3)
        data_string = ""
        data_string += str(len(numbers)) + ";"
        print("")
        message = '-> Quantity: %s (10 to the power of %s)' % (number + 3, i)
        print(message)
        print("Linear search: null")
        data_string += "null;"
        log_start = time.time()
        print(binary_search(numbers, number))
        result = time.time() - log_start
        print("Binary search:", result)
        data_string += str(result) + ";"
        log_start = time.time()
        print(recursive_binary_search(numbers, number))
        result = time.time() - log_start
        print("Recursive binary search:", result)
        data_string += str(result)
        with open("data.csv", "a") as file:
            file.write(data_string + "\n")
test_log()