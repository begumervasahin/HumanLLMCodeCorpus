from fractions import gcd
from random import randint
def fonk1(a1):
    return pow(a1, 2) + a1 + 1
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
            b2 = gcd(a1 - past_x, n)
            if b2 > 1:
                break
        else:
            b1.append(a1)
            continue
        break
    return b2 = = n
def fonk3(length):
    while True:
        b3 = str(randint(1, 9))
        for i in range(length - 2):
            b3 += str(randint(0, 9))
        b3 += str(randint(1, 5) * 2 - 1)
        if b3[-1] == '5':
            continue
        if sum(int(digit) for digit in b3) % b4 = = 0:
            continue
        if fonk2(int(b3)):
            break
    return int(b3)
if b5 = = "__main__":
    a2 = 10
    b6 = fonk3(a2)
    print("Generated prime number:", b6)