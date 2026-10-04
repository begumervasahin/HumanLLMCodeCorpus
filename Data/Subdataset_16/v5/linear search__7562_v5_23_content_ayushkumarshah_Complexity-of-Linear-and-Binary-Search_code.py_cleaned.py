import random
from time import time
b1 = random.sample(range(1_000_000), 100_000)
b2 = sorted(b1)
b3 = random.choice(b2)
b4 = []
b5 = []
b6 = []
b7 = []
def fonk1(values, target):
    for b8 in values:
        if b8 = = target:
            return True
    return False
def fonk2(values, target):
    for b8 in values:
        if b8 = = target:
            return True
        elif b8 > target:
            return False
    return False
def fonk3(values):
    b9 = values[0]
    for b8 in values[1:]:
        if b8 < b9:
            b9 = b8
    return b9
def fonk4(values, target):
    b12, b10 = 0, len(values) - 1
    while b12 <= b10:
        b11 = (b10 + b12)
        if values[b11] == target:
            return True
        elif target < values[b11]:
            b10 = b11 - 1
        else:
            b12 = b11 + 1
    return False
def fonk5(search_function, data, target):
    b13 = time()
    search_function(data, target)
    b14 = time()
    return b14 - b13
def fonk6():
    for size in range(10_000, 100_001, 10_000):
        b4.append(fonk5(linear_search, b1[:size], b3))
        b5.append(fonk5(sorted_linear_search, b2[:size], b3))
        b6.append(fonk5(find_smallest, b1[:size], None))
        b7.append(fonk5(binary_search, b2[:size], b3))
def fonk7(times, description):
    print(f"\n{description} times:")
    for elapsed_time in times:
        print(elapsed_time)
fonk6()
fonk7(b4, "Unsorted Linear Search")
fonk7(b5, "Sorted Linear Search")
fonk7(b6, "Finding Smallest Element")
fonk7(b7, "Binary Search")