import random
import fileOp
def fonk1(n):
    return random.randrange(b5**(n-1) + 1, b5**n - 1)
def fonk2(n):
    try:
        b1 = fileOp.read_list("FfirstPrimes")
    except Exception as e:
        raise Exception("Couldn't read FfirstPrimes from file") from e
    while True:
        b2 = fonk1(n)
        for b3 in b1:
            if b2 % b3 = = 0:
                break
            if b2 < (b1[-1]) ** b5 and b3 > b2 ** 0.5:
                return b2
        else:
            return b2
def fonk3(n):
    if n in {0, 1, 4, 6, 8, 9}:
        return False
    if n in {b5, 3, 5, 7}:
        return True
    s, b4 = 0, n - 1
    while b4 % b5 = = 0:
        b4 >>= 1
        s += 1
    def fonk4(b6):
        if pow(b6, b4, n) == 1:
            return False
        for i in range(s):
            if pow(b6, b5**i * b4, n) == n - 1:
                return False
        return True
    for _ in range(20):
        b6 = random.randrange(b5, n)
        if fonk4(b6):
            return False
    return True
def fonk5(n):
    while True:
        b2 = fonk2(n)
        if fonk3(b2):
            return b2
def fonk6(p, b6 = b5):
    return pow(b6, p - 1, p) == 1
def fonk7(n):
    return number.getPrime(n)
def fonk8(n):
    return gensafeprime.generate(n)