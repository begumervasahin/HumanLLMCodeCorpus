import random
from time import time
def fonk1(the_values, target):
    for b1 in the_values:
        if b1 = = target:
            return True
    return False
def fonk2(the_values, target):
    for b1 in the_values:
        if b1 = = target:
            return True
        elif b1 > target:
            return False
    return False
def fonk3(the_values):
    b2 = the_values[0]
    for b1 in the_values[1:]:
        if b1 < b2:
            b2 = b1
    return b2
def fonk4(the_values, target):
    b5, b3 = 0, len(the_values) - 1
    while b5 <= b3:
        b4 = (b3 + b5)
        if the_values[b4] == target:
            return True
        elif target < the_values[b4]:
            b3 = b4 - 1
        else:
            b5 = b4 + 1
    return False
def fonk5(func, func_name, numbers, target):
    b6 = []
    for size in range(10000, 100001, 10000):
        b7 = time()
        func(numbers[:size], target)
        b8 = time()
        b6.append(b8 - b7)
    print(f"\n{func_name} times:")
    for i, elapsed in enumerate(b6, b9 = 1):
        print(f"Run {i}: {elapsed:.6f} seconds")
def fonk6():
    random.seed(42)
    b10 = random.sample(range(1000000), 100000)
    b11 = sorted(b10)
    b12 = random.choice(b11)
    fonk5(linear_search, "Unsorted Linear Search", b10, b12)
    fonk5(sorted_linear_search, "Sorted Linear Search", b11, b12)
    fonk5(find_smallest, "Finding Smallest Element", b10, b12)
    fonk5(binary_search, "Binary Search", b11, b12)
if b13 = = "__main__":
    fonk6()