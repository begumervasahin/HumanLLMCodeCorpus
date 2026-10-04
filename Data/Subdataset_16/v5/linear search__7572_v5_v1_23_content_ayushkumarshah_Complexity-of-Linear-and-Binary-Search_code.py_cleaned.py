import random
from time import time
def fonk1(values, target):
    for b1 in values:
        if b1 = = target:
            return True
    return False
def fonk2(values, target):
    for b1 in values:
        if b1 = = target:
            return True
        elif b1 > target:
            return False
    return False
def fonk3(values):
    b2 = values[0]
    for b1 in values[1:]:
        if b1 < b2:
            b2 = b1
    return b2
def fonk4(values, target):
    a1 = 0
    b3 = len(values) - 1
    while a1 <= b3:
        b4 = (b3 + a1)
        if values[b4] == target:
            return True
        elif target < values[b4]:
            b3 = b4 - 1
        else:
            a1 = b4 + 1
    return False
random.seed(42)
b5 = random.sample(range(1000000), 100000)
b6 = sorted(b5)
b7 = random.choice(b6)
def fonk5(search_func, values, target):
    b8 = time()
    search_func(values, target)
    b9 = time()
    return b9 - b8
b10 = {
    "unsorted_linear_search": [],
    "sorted_linear_search": [],
    "find_smallest": [],
    "binary_search": []
}
for i in range(10000, 100001, 10000):
    b10["unsorted_linear_search"].append(fonk5(linear_search, b5[:i], b7))
    b10["sorted_linear_search"].append(fonk5(sorted_linear_search, b6[:i], b7))
    b10["find_smallest"].append(fonk5(find_smallest, b5[:i], b7))
    b10["binary_search"].append(fonk5(binary_search, b6[:i], b7))
def fonk6(title, times):
    print(f"\n{title} times:")
    for time_elapsed in times:
        print(time_elapsed)
fonk6("Unsorted Linear Search", b10["unsorted_linear_search"])
fonk6("Sorted Linear Search", b10["sorted_linear_search"])
fonk6("Finding Smallest Element", b10["find_smallest"])
fonk6("Binary Search", b10["binary_search"])