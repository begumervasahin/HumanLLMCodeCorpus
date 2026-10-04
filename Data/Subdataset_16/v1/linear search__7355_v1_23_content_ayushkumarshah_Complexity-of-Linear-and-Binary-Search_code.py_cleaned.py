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
    a1 = 0
    b3 = len(theValues) - 1
    while a1 <= b3:
        b4 = (b3 + a1)
        if theValues[b4] == target:
            return True
        elif target < theValues[b4]:
            b3 = b4 - 1
        else:
            a1 = b4 + 1
    return False
b5 = random.sample(range(1000000), 100000)
b6 = sorted(b5)
b7 = random.choice(b6)
b8 = []
b9 = []
b10 = []
b11 = []
for i in range(10000, 100001, 10000):
    b12 = time()
    fonk1(b5[:i], b7)
    b13 = time()
    b8.append(b13 - b12)
    b12 = time()
    fonk2(b6[:i], b7)
    b13 = time()
    b9.append(b13 - b12)
    b12 = time()
    fonk3(b5[:i])
    b13 = time()
    b10.append(b13 - b12)
    b12 = time()
    fonk4(b6[:i], b7)
    b13 = time()
    b11.append(b13 - b12)
print("\nUnsorted Linear Search times")
for time_elapsed in b8:
    print(time_elapsed)
print("\nSorted Linear Search times")
for time_elapsed in b9:
    print(time_elapsed)
print("\nFinding Smallest element times")
for time_elapsed in b10:
    print(time_elapsed)
print("\nBinary Search times")
for time_elapsed in b11:
    print(time_elapsed)