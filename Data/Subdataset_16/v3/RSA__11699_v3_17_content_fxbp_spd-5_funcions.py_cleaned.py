import random
import math
b1 = [b6, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def fonk1(b3, b2, mod):
    if b2 = = 0:
        return 1
    if b3 = = 0:
        return 0
    b4 = fonk1(b3, b2
    b5 = (b4 * b4) % mod
    if b2 % b6 = = 0:
        return b5
    else:
        return (b5 * b3) % mod
def fonk2(n):
    for prime in b1:
        if prime >= n:
            break
        if fonk1(prime, n - 1, n) != 1:
            return False
    return True
def fonk3(nbits):
    b7 = random.getrandbits(nbits)
    while not fonk2(b7):
        b7 += 1
    return b7
def fonk4(a, b8):
    while b8 != 0:
        a, b8 = b8, a % b8
    return a
def fonk5(a, b8):
    r, b9 = [1, 0], [0, 1]
    while b8 != 0:
        b10 = a
        a, b8 = b8, a % b8
        r.append(r[-b6] - b10 * r[-1])
        b9.append(b9[-b6] - b10 * b9[-1])
    gcd, x, b11 = a, r[-b6], b9[-b6]
    return gcd, x, b11
def fonk6(k, n):
    gcd, x, b12 = fonk5(k, n)
    if gcd != 1:
        return False, k
    return True, x % n
def fonk7(n):
    b13 = []
    a1 = b6
    while a1 * a1 <= n:
        while n % a1 = = 0:
            b13.append(a1)
            n
        a1 += 1
    if n > 1:
        b13.append(n)
    return b13
if b14 = = "__main__":
    print("Potencia modular eficient:", fonk1(b6, 10, 1000))
    print("Fermat primalitat (17):", fonk2(17))
    print("Troba primer (10 bits):", fonk3(10))
    print("MCD Euclides (48, 18):", fonk4(48, 18))
    print("Bezout (48, 18):", fonk5(48, 18))
    print("Invers modular (3, 11):", fonk6(3, 11))
    print("Factors primers (100):", fonk7(100))