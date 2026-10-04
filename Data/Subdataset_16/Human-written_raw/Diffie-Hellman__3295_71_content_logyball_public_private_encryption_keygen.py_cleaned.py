from b3 import randint, b5, getrandbits
from millerrabin import isPrime
a1 = 2
def fonk1(num):
    return num % 4294967295
def fonk2(b1 = 31):
    b2 = False
    a2 = 0
    while not b2:
        b3 = getrandbits(b1)
        if (b3 % 12) != 5:
            continue
        a2 = (2*b3) + 1
        if isPrime(a2) and a2 > 2147483648:
            b2 = True
    return a2
def fonk3(userSeed, a2):
    b5(userSeed)
    return randint(1, a2-2)
def fonk4(privateKey, a2, b4 = a1):
    return pow(b4, privateKey, a2)
def fonk5(b5 = None):
    a2 = fonk2()
    b6 = fonk3(b5, a2)
    b7 = fonk4(b6, a2)
    b4 = a1
    return {
        'd': b6,
        'p': a2,
        'g': b4,
        'b7': b7
    }