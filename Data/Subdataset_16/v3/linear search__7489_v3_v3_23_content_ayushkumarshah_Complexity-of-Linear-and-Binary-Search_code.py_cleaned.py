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
    b5, b3 = 0, len(values) - 1
    while b5 <= b3:
        b4 = (b5 + b3)
        if values[b4] == target:
            return True
        elif target < values[b4]:
            b3 = b4 - 1
        else:
            b5 = b4 + 1
    return False
random.seed(42)
b6 = random.sample(range(1000000), 100000)
b7 = sorted(b6)
b8 = random.choice(b7)
def fonk5(func, func_name, numbers, target):
    b9 = []
    for size in range(10000, 100001, 10000):
        b10 = time()
        func(numbers[:size], target)
        b11 = time()
        b9.append(b11 - b10)
    print(f"\n{func_name} times:")
    for i, elapsed_time in enumerate(b9):
        print(f"Size {10000 * (i + 1)}: {elapsed_time:.6f} seconds")
fonk5(linear_search, "Unsorted Linear Search", b6, b8)
fonk5(sorted_linear_search, "Sorted Linear Search", b7, b8)
fonk5(find_smallest, "Finding Smallest Element", b6, b8)
fonk5(binary_search, "Binary Search", b7, b8)