import random
import math
b1 = [b5, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def fonk1(b3, b2, p):
    if b2 = = 0:
        return 1
    elif b3 = = 0:
        return 0
    else:
        b4 = fonk1(b3, b2
        if b2 % b5 = = 0:
            return (b4 * b4) % p
        else:
            return (b4 * b4 * b3) % p
def fonk2(n):
    a1 = 0
    while a1 < len(b1) and b1[a1] < n:
        b6 = b1[a1]
        b7 = fonk1(b6, n - 1, n)
        a1 += 1
        if b7 != 1:
            return False
    return True
def fonk3(nbits):
    b8 = random.getrandbits(nbits)
    while not fonk2(b8):
        b8 += 1
    return b8
def fonk4(b10, b11):
    b9 = b10 % b11
    while b9 != 0:
        b10 = b11
        b11 = b9
        b9 = b10 % b11
    return b11
def fonk5(b10, b11):
    b9 = b10 % b11
    b12 = b10
    a1 = b5
    b13 = [1, 0]
    b14 = [0, 1]
    while b9 != 0:
        b13.append(b12 * b13[a1 - 1] + b13[a1 - b5])
        b14.append(b12 * b14[a1 - 1] + b14[a1 - b5])
        b10 = b11
        b11 = b9
        b9 = b10 % b11
        b12 = b10
        a1 += 1
    b15 = b14[a1 - 1]
    b16 = b13[a1 - 1]
    if (a1 - 1) % b5 = = 0:
        b15 *= -1
    else:
        b16 *= -1
    return b11, b16, b15
def fonk6(k, n):
    mcd, b13, b14 = fonk5(k, n)
    if mcd != 1:
        return False, k
    else:
        return True, (b13 % n)
def fonk7(b18):
    b17 = []
    if b18 >= b5:
        a2 = b5
        while a2 <= math.sqrt(b18):
            if b18 % a2 = = 0:
                b17.append(a2)
                b18 = b18 / a2
            else:
                a2 = a2 + 1
        b17.append(int(b18))
    return b17
print("Potencia modular eficient:", fonk1(b5, 10, 1000))
print("Fermat primalitat (17):", fonk2(17))
print("Troba primer (10 bits):", fonk3(10))
print("MCD Euclides (48, 18):", fonk4(48, 18))
print("Bezoud (48, 18):", fonk5(48, 18))
print("Invers modular (3, 11):", fonk6(3, 11))
print("Factors primers (100):", fonk7(100))