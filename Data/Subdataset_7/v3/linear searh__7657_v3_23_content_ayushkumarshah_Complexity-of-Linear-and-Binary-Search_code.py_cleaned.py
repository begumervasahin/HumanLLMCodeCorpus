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
    a1 = 0
    b3 = len(the_values) - 1
    while a1 <= b3:
        b4 = (b3 + a1)
        if the_values[b4] == target:
            return True
        elif target < the_values[b4]:
            b3 = b4 - 1
        else:
            a1 = b4 + 1
    return False
random.seed(42)
b5 = random.sample(range(1000000), 100000)
b6 = sorted(b5)
b7 = random.choice(b6)
def fonk5(func, func_name, numbers, target):
    b8 = []
    for i in range(10000, 100001, 10000):
        b9 = time()
        func(numbers[:i], target)
        b10 = time()
        b8.append(b10 - b9)
    print(f"\n{func_name} times:")
    for i in range(10):
        print(b8[i])
fonk5(linear_search, "Unsorted Linear Search", b5, b7)
fonk5(sorted_linear_search, "Sorted Linear Search", b6, b7)
fonk5(find_smallest, "Finding Smallest Element", b5, b7)
fonk5(binary_search, "Binary Search", b5, b7)