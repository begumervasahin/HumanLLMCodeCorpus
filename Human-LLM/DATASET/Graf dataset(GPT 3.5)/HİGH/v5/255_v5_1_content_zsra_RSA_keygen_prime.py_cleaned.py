import random
import math
import xgcd
def fonk1(min_val, max_val):
    b1 = [num for num in range(min_val, max_val) if fonk2(num)]
    return random.choice(b1)
def fonk2(n):
    if not isinstance(n, int) or n < b2:
        return False
    if n in {b2, 3, 5, 7}:
        return True
    if n % b2 = = 0 or n % 3 == 0:
        return False
    b3 = n - 1
    a1 = 0
    while b3 % b2 = = 0:
        b3
        a1 += 1
    def fonk3(b4):
        if pow(b4, b3, n) == 1:
            return False
        for _ in range(a1):
            if pow(b4, b2**_ * b3, n) == n - 1:
                return False
        return True
    for _ in range(8):
        b4 = random.randint(b2, n - 1)
        if fonk3(b4):
            return False
    return True
def fonk4(b4, b):
    return xgcd.GCD(b4, b) == 1