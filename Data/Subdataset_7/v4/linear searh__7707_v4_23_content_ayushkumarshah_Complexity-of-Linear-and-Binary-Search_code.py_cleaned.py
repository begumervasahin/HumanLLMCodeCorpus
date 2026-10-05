import random
from time import time
b1 = random.sample(range(1000000), 100000)
b2 = sorted(b1)
b3 = random.choice(b2)
b4 = []
b5 = []
b6 = []
b7 = []
def fonk1(the_values, target):
    for b8 in the_values:
        if b8 = = target:
            return True
    return False
def fonk2(the_values, target):
    for b8 in the_values:
        if b8 = = target:
            return True
        elif b8 > target:
            return False
    return False
def fonk3(the_values):
    b9 = the_values[0]
    for b8 in the_values[1:]:
        if b8 < b9:
            b9 = b8
    return b9
def fonk4(the_values, target):
    a1 = 0
    b10 = len(the_values) - 1
    while a1 <= b10:
        b11 = (b10 + a1)
        if the_values[b11] == target:
            return True
        elif target < the_values[b11]:
            b10 = b11 - 1
        else:
            a1 = b11 + 1
    return False
for i in range(10000, 100001, 10000):
    b12 = time()
    fonk1(b1[:i], b3)
    b13 = time()
    b4.append(b13 - b12)
print("\nUnsorted Linear Search times:")
for time_val in b4:
    print(time_val)
for i in range(10000, 100001, 10000):
    b12 = time()
    fonk2(b2[:i], b3)
    b13 = time()
    b5.append(b13 - b12)
print("\nSorted Linear Search times:")
for time_val in b5:
    print(time_val)
for i in range(10000, 100001, 10000):
    b12 = time()
    fonk3(b1[:i])
    b13 = time()
    b6.append(b13 - b12)
print("\nFinding Smallest Element times:")
for time_val in b6:
    print(time_val)
for i in range(10000, 100001, 10000):
    b12 = time()
    fonk4(b2[:i], b3)
    b13 = time()
    b7.append(b13 - b12)
print("\nBinary Search times:")
for time_val in b7:
    print(time_val)