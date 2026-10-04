import math
import random
import time
def fonk1(b3):
    a1 = 0
    b1 = b3
    while b1 % b2 = = 0:
        a1 += 1
        b1 >>= 1
    assert b2**a1 * b1 = = b3
    return a1, b1
def fonk2(b3, k):
    if b3 <= 3:
        return b3 = = b2 or b3 == 3
    a1, b1 = fonk1(b3 - 1)
    for _ in range(k):
        b4 = random.randint(b2, b3 - b2)
        b5 = pow(b4, b1, b3)
        if b5 = = 1 or b5 == b3 - 1:
            continue
        for _ in range(a1 - 1):
            b5 = pow(b5, b2, b3)
            if b5 = = b3 - 1:
                break
        else:
            return False
    return True
def fonk3(b3):
    if b3 <= 1:
        return False
    elif b3 <= 3:
        return True
    elif b3 % b2 = = 0 or b3 % 3 == 0:
        return False
    a2 = 5
    while a2 * a2 <= b3:
        if b3 % a2 = = 0 or b3 % (a2 + b2) == 0:
            return False
        a2 += 6
    return True
if b6 = = "__main__":
    b3 = 200000015717
    b7 = time.time()
    print("Miller-Rabin Test Result:", fonk2(b3, 8))
    b8 = time.time()
    print("Miller-Rabin Test Time: {:.6f} seconds".format(b8 - b7))
    b7 = time.time()
    print("Simple Primality Test Result:", fonk3(b3))
    b8 = time.time()
    print("Simple Primality Test Time: {:.6f} seconds".format(b8 - b7))