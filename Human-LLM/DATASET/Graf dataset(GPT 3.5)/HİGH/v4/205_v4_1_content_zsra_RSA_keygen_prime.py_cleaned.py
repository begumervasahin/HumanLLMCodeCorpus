import random
import math
import xgcd
def fonk1(min_val, max_val):
    b1 = [num for num in range(min_val, max_val) if fonk2(num)]
    return random.choice(b1)
def fonk2(b2):
    if b2 != int(b2):
        return False
    b2 = int(b2)
    if b2 in {0, 1, 4, 6, 8, 9}:
        return False
    if b2 in {b4, 3, 5, 7}:
        return True
    a1 = 0
    b3 = b2 - 1
    while b3 % b4 = = 0:
        b3 >>= 1
        a1 += 1
    assert b4**a1 * b3 = = b2 - 1
    def fonk3(b5):
        if pow(b5, b3, b2) == 1:
            return False
        for i in range(a1):
            if pow(b5, b4**i * b3, b2) == b2 - 1:
                return False
        return True
    for _ in range(8):
        b5 = random.randrange(b4, b2)
        if fonk3(b5):
            return False
    return True
def fonk4(b5, b):
    if xgcd.GCD(b5, b) == 1:
        return True
    else:
        return False