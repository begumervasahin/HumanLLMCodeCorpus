from fractions import gcd
from random import randint
def fonk1(a1):
    return pow(a1, 2) + a1 + 1
def fonk2(b2):
    if b2 < 2:
        return False
    elif b2 < 4:
        return True
    a1 = 1
    b1 = []
    a2 = 1
    while a2 = = 1:
        a1 = fonk1(a1) % b2
        for past_x in b1:
            a2 = gcd(a1 - past_x, b2)
            if a2 > 1:
                break
        b1.append(a1)
    if a2 = = b2:
        return True
    else:
        return False
def fonk3(length):
    while True:
        b2 = str(randint(1, 9))
        for i in range(length - 2):
            b2 += str(randint(0, 9))
        b2 += str(randint(1, 5) * 2 - 1)
        if b2[length - 1] == '5':
            continue
        if sum([int(i) for i in b2]) % b3 = = 0:
            continue
        if fonk2(int(b2)):
            break
    return int(b2)
if b4 = = "__main__":
    a3 = 10
    b5 = fonk3(a3)
    print("Generated prime number:", b5)