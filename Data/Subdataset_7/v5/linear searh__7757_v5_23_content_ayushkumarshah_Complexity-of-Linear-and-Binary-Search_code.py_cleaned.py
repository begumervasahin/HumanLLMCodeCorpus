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
    return min(the_values)
def fonk4(the_values, target):
    a1 = 0
    b2 = len(the_values) - 1
    while a1 <= b2:
        b3 = (b2 + a1)
        if the_values[b3] == target:
            return True
        elif target < the_values[b3]:
            b2 = b3 - 1
        else:
            a1 = b3 + 1
    return False
b4 = random.sample(range(1000000), 100000)
b5 = sorted(b4)
b6 = random.choice(b5)
b7 = []
b8 = []
b9 = []
b10 = []
b11 = range(10000, 100001, 10000)
for size in b11:
    b12 = time()
    fonk1(b4[:size], b6)
    b13 = time()
    b7.append(b13 - b12)
    b12 = time()
    fonk2(b5[:size], b6)
    b13 = time()
    b8.append(b13 - b12)
    b12 = time()
    fonk3(b4[:size])
    b13 = time()
    b9.append(b13 - b12)
    b12 = time()
    fonk4(b5[:size], b6)
    b13 = time()
    b10.append(b13 - b12)
print("\nUnsorted Linear Search times:")
for time_val in b7:
    print(time_val)
print("\nSorted Linear Search times:")
for time_val in b8:
    print(time_val)
print("\nFinding Smallest Element times:")
for time_val in b9:
    print(time_val)
print("\nBinary Search times:")
for time_val in b10:
    print(time_val)