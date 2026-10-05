import math
import random
import time
def fonk1(a3):
    a1 = 0
    b1 = a3
    while b1 % b2 = = 0:
        a1 += 1
        b1
    assert b2**a1 * b1 = = a3
    return a1, b1
def fonk2(a3, k):
    if a3 <= 3:
        return False
    a1, b1 = fonk1(a3 - 1)
    for _ in range(k):
        b3 = random.randint(b2, a3 - b2)
        b4 = pow(b3, b1, a3)
        if b4 = = 1 or b4 == a3 - 1:
            continue
        b5 = False
        for _ in range(a1 - 1):
            b4 = pow(b4, b2, a3)
            if b4 = = a3 - 1:
                b5 = True
                break
        if not b5:
            return False
    return True
def fonk3(a3):
    if a3 <= 1:
        return False
    elif a3 <= 3:
        return True
    elif a3 % b2 = = 0 or a3 % 3 == 0:
        return False
    a2 = 5
    while a2 * a2 <= a3:
        if a3 % a2 = = 0 or a3 % (a2 + b2) == 0:
            return False
        a2 += 6
    return True
a3 = 200000015717
b6 = time.time()
print("Miller-Rabin Test Result:", fonk2(a3, 8))
b7 = time.time()
print("Miller-Rabin Primality Test Time:", b7 - b6)
b6 = time.time()
print("Simple Primality Test Result:", fonk3(a3))
b7 = time.time()
print("Simple Primality Test Time:", b7 - b6)