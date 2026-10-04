import random
from time import time
b1 = random.sample(range(1000000), 100000)
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
def fonk5():
    for i in range(10000, 100001, 10000):
        b13 = time()
        fonk1(b1[:i], b3)
        b14 = time()
        b4.append(b14 - b13)
        b13 = time()
        fonk2(b2[:i], b3)
        b14 = time()
        b5.append(b14 - b13)
        b13 = time()
        fonk3(b1[:i])
        b14 = time()
        b6.append(b14 - b13)
        b13 = time()
        fonk4(b2[:i], b3)
        b14 = time()
        b7.append(b14 - b13)
fonk5()
def fonk6(times, description):
    print(f"\n{description} times")
    for time in times:
        print(time)
fonk6(b4, "Unsorted Linear Search")
fonk6(b5, "Sorted Linear Search")
fonk6(b6, "Finding Smallest Element")
fonk6(b7, "Binary Search")