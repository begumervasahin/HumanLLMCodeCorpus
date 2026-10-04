import random
from time import time
def fonk1(values, target):
    return target in values
def fonk2(values, target):
    for b1 in values:
        if b1 = = target:
            return True
        elif b1 > target:
            return False
    return False
def fonk3(values):
    return min(values)
def fonk4(values, target):
    b4, b2 = 0, len(values) - 1
    while b4 <= b2:
        b3 = (b2 + b4)
        if values[b3] == target:
            return True
        elif target < values[b3]:
            b2 = b3 - 1
        else:
            b4 = b3 + 1
    return False
b5 = random.sample(range(1000000), 100000)
b6 = sorted(b5)
b7 = random.choice(b6)
b8 = []
b9 = []
b10 = []
b11 = []
for size in range(10000, 100001, 10000):
    b12 = b5[:size]
    b13 = b6[:size]
    b14 = time()
    fonk1(b12, b7)
    b15 = time()
    b8.append(b15 - b14)
    b14 = time()
    fonk2(b13, b7)
    b15 = time()
    b9.append(b15 - b14)
    b14 = time()
    fonk3(b12)
    b15 = time()
    b10.append(b15 - b14)
    b14 = time()
    fonk4(b13, b7)
    b15 = time()
    b11.append(b15 - b14)
def fonk5(title, times):
    print(f"\n{title}")
    for time_elapsed in times:
        print(time_elapsed)
fonk5("Unsorted Linear Search times", b8)
fonk5("Sorted Linear Search times", b9)
fonk5("Finding Smallest Element times", b10)
fonk5("Binary Search times", b11)