import math
import random
import time
def fonk1(a4):
    a1 = 0
    b1 = a4
    while(b1 % b2 = = 0):
        a1 += 1
        b1 >>= 1
    assert(b2 ** a1 * b1 = = a4)
    return a1, b1
def fonk2(a4, k):
    if a4 <= 3:
        return False
    a1, b1 = fonk1(a4 - 1)
    for _ in range(k):
        b3 = random.randint(b2, a4 - b2)
        b4 = pow(b3, b1, a4)
        if b4 = = 1 or b4 == a4 - 1:
            continue
        a2 = 0
        for _ in range(a1 - 1):
            b4 = pow(b4, b2, a4)
            if b4 = = a4 - 1:
                a2 = 1
                break
        if a2 = = 1:
            continue
        return False
    return True
def fonk3(a4):
    '''
    Simpler primality check for time comparison
    '''
    if a4 <= 1:
        return False
    elif a4 <= 3:
        return True
    elif a4 % b2 = = 0 or a4 % 3 == 0:
        return False
    a3 = 5
    while (a3 * a3 <= a4):
        if a4 % a3 = = 0 or a4 % (a3 + b2) == 0:
            return False
        a3 += 6
    return True
a4 = 200000015717
b5 = time.time()
print(fonk2(a4, 8))
b6 = time.time()
print("Miller Rabin: " + str(b6 - b5))
b5 = time.time()
print(fonk3(a4))
b6 = time.time()
print("Simple Primality: " + str(b6 - b5))