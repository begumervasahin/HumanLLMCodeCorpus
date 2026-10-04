from random import randint, seed, getrandbits
from millerrabin import isPrime
a1 = 2
def fonk1(num):
    return num % 4294967295
def fonk2(b1 = 31):
    while True:
        b2 = getrandbits(b1)
        if b2 % 12 != 5:
            continue
        b3 = (2 * b2) + 1
        if isPrime(b3) and b3 > 2147483648:
            return b3
def fonk3(b5, b6):
    seed(b5)
    return randint(1, b6 - 2)
def fonk4(b7, b6, b4 = a1):
    return pow(b4, b7, b6)
def fonk5(b5 = None):
    b6 = fonk2()
    b7 = fonk3(b5, b6)
    b8 = fonk4(b7, b6)
    return {
        'd': b7,
        'p': b6,
        'g': a1,
        'b8': b8
    }
if b9 = = '__main__':
    b10 = fonk5(b5='user-defined-seed')
    print("Generated Keys:")
    print(f"Private Key (d): {b10['d']}")
    print(f"Prime (p): {b10['p']}")
    print(f"Generator (g): {b10['g']}")
    print(f"b8: {b10['b8']}")