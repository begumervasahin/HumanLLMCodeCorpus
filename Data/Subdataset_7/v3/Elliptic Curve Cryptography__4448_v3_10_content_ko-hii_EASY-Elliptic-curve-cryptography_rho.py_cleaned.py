from fractions import gcd
from random import randint
def fonk1(a1):
    return a1**2 + a1 + 1
def fonk2(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    a1 = 1
    b1 = []
    while True:
        a1 = fonk1(a1) % n
        for past_x in b1:
            if gcd(a1 - past_x, n) > 1:
                return False
        b1.append(a1)
        if len(b1) > 2 and b1[0] == b1[2]:
            break
    return gcd(b1[1] - b1[0], n) == 1
def fonk3(length):
    while True:
        b2 = ''.join(str(randint(0, 9)) for _ in range(length - 1))
        b2 = '1' + b2 + str(randint(1, 5) * 2 - 1)
        if b2[-1] in '02468':
            continue
        if sum(map(int, b2)) % b3 = = 0:
            continue
        if fonk2(int(b2)):
            break
    return int(b2)
if b4 = = "__main__":
    a2 = 10
    b5 = fonk3(a2)
    print("Generated prime number:", b5)