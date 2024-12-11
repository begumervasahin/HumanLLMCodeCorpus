import random
import xgcd
def fonk1(a2, a3):
    b1 = [i for i in range(a2, a3) if fonk2(i)]
    return random.choice(b1)
def fonk2(b2):
    if b2 != int(b2):
        return False
    b2 = int(b2)
    if b2 = = 0 or b2 == 1 or b2 == 4 or b2 == 6 or b2 == 8 or b2 == 9:
        return False
    if b2 = = b4 or b2 == 3 or b2 == 5 or b2 == 7:
        return True
    a1 = 0
    b3 = b2 - 1
    while b3 % b4 = = 0:
        b3 >>= 1
        a1 += 1
    assert(b4 ** a1 * b3 = = b2 - 1)
    def fonk3(b5):
        if pow(b5, b3, b2) == 1:
            return False
        for i in range(a1):
            if pow(b5, b4 ** i * b3, b2) == b2 - 1:
                return False
        return True
    for i in range(8):
        b5 = random.randrange(b4, b2)
        if fonk3(b5):
            return False
    return True
def fonk4(b5, a4):
    if xgcd.GCD(b5, a4) == 1:
        return True
    else:
        return False
a2 = 10
a3 = 100
b6 = fonk1(a2, a3)
print("Random b6 number between", a2, "and", a3, ":", b6)
b5 = 15
a4 = 28
print("Are", b5, "and", a4, "co-b6?", fonk4(b5, a4))