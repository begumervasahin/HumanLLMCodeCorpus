import random
from time import time
def fonk1(theValues, target):
    for b1 in theValues:
        if b1 = = target:
            return True
    return False
def fonk2(theValues, target):
    for b1 in theValues:
        if b1 = = target:
            return True
        elif b1 > target:
            return False
    return False
def fonk3(theValues):
    b2 = theValues[0]
    for b1 in theValues[1:]:
        if b1 < b2:
            b2 = b1
    return b2
def fonk4(theValues, target):
    b5, b3 = 0, len(theValues) - 1
    while b5 <= b3:
        b4 = (b3 + b5)
        if theValues[b4] == target:
            return True
        elif target < theValues[b4]:
            b3 = b4 - 1
        else:
            b5 = b4 + 1
    return False
b6 = random.sample(range(1000000), 100000)
b7 = sorted(b6)
b8 = random.choice(b7)
b9 = []
b10 = []
b11 = []
b12 = []
for i in range(10000, 100001, 10000):
    b13 = time()
    fonk1(b6[:i], b8)
    b14 = time()
    b9.append(b14 - b13)
    b13 = time()
    fonk2(b7[:i], b8)
    b14 = time()
    b10.append(b14 - b13)
    b13 = time()
    fonk3(b6[:i])
    b14 = time()
    b11.append(b14 - b13)
    b13 = time()
    fonk4(b7[:i], b8)
    b14 = time()
    b12.append(b14 - b13)
print("\nUnsorted Linear Search times")
for time_elapsed in b9:
    print(time_elapsed)
print("\nSorted Linear Search times")
for time_elapsed in b10:
    print(time_elapsed)
print("\nFinding Smallest Element times")
for time_elapsed in b11:
    print(time_elapsed)
print("\nBinary Search times")
for time_elapsed in b12:
    print(time_elapsed)