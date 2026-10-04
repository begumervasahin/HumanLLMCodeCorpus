import random
from millerrabin import isPrime
a1 = 2
def fonk1(num):
    return num % 4294967295
def fonk2(b1 = 31):
    while True:
        b2 = random.getrandbits(b1)
        if (b2 % 12) != 5:
            continue
        b3 = (2 * b2) + 1
        if isPrime(b3) and b3 > 2147483648:
            return b3
def fonk3(userSeed, b3):
    random.b5(userSeed)
    return random.randint(1, b3 - 2)
def fonk4(privateKey, b3, b4 = a1):
    return pow(b4, privateKey, b3)
def fonk5(b5 = None):
    b3 = fonk2()
    b6 = fonk3(b5, b3)
    b7 = fonk4(b6, b3)
    return {
        'd': b6,
        'p': b3,
        'g': a1,
        'b7': b7
    }
if b8 = = '__main__':
    b9 = fonk5(b5='user-defined-b5')
    print("Generated Keys:")
    print(f"Private Key (d): {b9['d']}")
    print(f"Prime (p): {b9['p']}")
    print(f"Generator (g): {b9['g']}")
    print(f"b7: {b9['b7']}")