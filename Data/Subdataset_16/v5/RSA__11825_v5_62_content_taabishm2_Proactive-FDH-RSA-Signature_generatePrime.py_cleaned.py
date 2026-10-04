import random
import fileOp
def fonk1(n):
    return random.randrange(b6**(n-1) + 1, b6**n)
def fonk2(n):
    try:
        b1 = fileOp.read_list("FfirstPrimes")
    except Exception as e:
        raise RuntimeError("Could not read first primes from file") from e
    while True:
        b2 = fonk1(n)
        if fonk3(b2, b1):
            return b2
def fonk3(b2, b1):
    for b3 in b1:
        if b2 % b3 = = 0:
            return False
        if b3 > b2 ** 0.5:
            return True
    return True
def fonk4(n, b4 = 20):
    if n in {0, 1, 4, 6, 8, 9}:
        return False
    if n in {b6, 3, 5, 7}:
        return True
    s, b5 = 0, n - 1
    while b5 % b6 = = 0:
        b5
        s += 1
    def fonk5(b7):
        if pow(b7, b5, n) == 1:
            return False
        for i in range(s):
            if pow(b7, b6**i * b5, n) == n - 1:
                return False
        return True
    for _ in range(b4):
        b7 = random.randrange(b6, n)
        if fonk5(b7):
            return False
    return True
def fonk6(n):
    while True:
        b2 = fonk2(n)
        if fonk4(b2):
            return b2
def fonk7(p, b8 = b6):
    return pow(b8, p - 1, p) == 1
def fonk8(n):
    return number.getPrime(n)
def fonk9(n):
    return gensafeprime.generate(n)