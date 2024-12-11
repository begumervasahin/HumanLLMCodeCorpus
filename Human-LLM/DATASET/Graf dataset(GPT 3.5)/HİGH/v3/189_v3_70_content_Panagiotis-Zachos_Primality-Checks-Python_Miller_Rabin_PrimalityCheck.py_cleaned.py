import math
import random
import time
def fonk1(a3):
    a1 = 0
    while a3 % b1 = = 0:
        a1 += 1
        a3
    return a1, a3
def fonk2(a3, k):
    if a3 <= 3:
        return a3 > 1
    r, b2 = fonk1(a3 - 1)
    for _ in range(k):
        b3 = random.randint(b1, a3 - b1)
        b4 = pow(b3, b2, a3)
        if b4 = = 1 or b4 == a3 - 1:
            continue
        for _ in range(r - 1):
            b4 = pow(b4, b1, a3)
            if b4 = = a3 - 1:
                break
        else:
            return False
    return True
def fonk3(a3):
    if a3 <= 1:
        return False
    elif a3 <= 3:
        return True
    elif a3 % b1 = = 0 or a3 % 3 == 0:
        return False
    a2 = 5
    while a2 * a2 <= a3:
        if a3 % a2 = = 0 or a3 % (a2 + b1) == 0:
            return False
        a2 += 6
    return True
if b5 = = "__main__":
    a3 = 200000015717
    b6 = time.time()
    print("Miller-Rabin Test Result:", fonk2(a3, 8))
    b7 = time.time()
    print("Miller-Rabin Test Time: {:.6f} seconds".format(b7 - b6))
    b6 = time.time()
    print("Simple Primality Test Result:", fonk3(a3))
    b7 = time.time()
    print("Simple Primality Test Time: {:.6f} seconds".format(b7 - b6))