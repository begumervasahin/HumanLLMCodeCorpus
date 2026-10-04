import time
import math
def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst)
        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint+1:], target)
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
        if target == lst[i]:
            return i
    return None
def test_log():
    for i in range(10, 19):
        numbers = range(int(math.pow(10, i)))
        number = int(math.pow(10, i)) - 3
        datastring = ""
        datastring += str(len(numbers))
        datastring += ";"
        print("")
        message = '-> Quantity: %s (10 to the power of %s)' % (number + 3, i)
        print(message)
        print("Linear search: ", "null")
        datastring += "null"
        datastring += ";"
        log_start = time.time()
        print(binary_search(numbers, number))
        result = time.time() - log_start
        print("Binary search: ", result)
        datastring += str(result)
        datastring += ";"
        log_start = time.time()
        print(recursive_binary_search(numbers, number))
        result = time.time() - log_start
        print("Recursive binary search: ", result)
        datastring += str(result)
        with open("data.csv", "a") as file:
            file.write(datastring + "\n")
test_log()