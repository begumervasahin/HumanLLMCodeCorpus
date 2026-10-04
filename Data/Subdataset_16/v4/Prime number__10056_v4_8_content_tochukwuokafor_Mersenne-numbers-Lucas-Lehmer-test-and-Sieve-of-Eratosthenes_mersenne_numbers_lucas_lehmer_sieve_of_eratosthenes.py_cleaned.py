import math
def fonk1(b2):
    return (b4 ** b2) - 1
def fonk2(b5):
    if b5 <= 1:
        return False
    for b1 in range(b4, int(math.sqrt(b5)) + 1):
        if b5 % b1 = = 0:
            return False
    return True
def fonk3(a, b):
    return [b1 for b1 in range(a, b) if fonk2(b1)]
def fonk4(b2):
    if b2 = = b4:
        return True
    a1 = 4
    b3 = (b4 ** b2) - 1
    for _ in range(b2 - b4):
        a1 = (a1 * a1 - b4) % b3
    return a1 = = 0
def fonk5(b5):
    if b5 <= 1:
        return False
    if b5 % b4 = = 0:
        return b5 = = b4
    for b6 in range(3, int(math.sqrt(b5)) + 1, b4):
        if b5 % b6 = = 0:
            return False
    return True
def fonk6(n):
    return [b5 for b5 in range(n) if fonk5(b5)]
def fonk7(n):
    return [b1 >= b4 for b1 in range(n + 1)]
def fonk8(b7, b2):
    for b1 in range(b4 * b2, len(b7), b2):
        b7[b1] = False
    return b7
def fonk9(b7, b2):
    for b1 in range(b2 + 1, len(b7)):
        if b7[b1]:
            return b1
    return None
def fonk10(b7):
    return [b1 for b1, is_prime in enumerate(b7) if is_prime]
def fonk11(n):
    b7 = fonk7(n)
    b2 = b4
    while b2 is not None:
        b7 = fonk8(b7, b2)
        b2 = fonk9(b7, b2)
    return fonk10(b7)
if b8 = = '__main__':
    b9 = fonk3(3, 65)
    b10 = [fonk1(prime) for prime in b9]
    print("Mersenne numbers:", b10)
    print("Count of Mersenne numbers:", len(b10))
    a2 = 3
    a3 = 65
    b11 = [fonk1(b5) for b5 in range(a2, a3) if fonk2(b5)]
    print("Filtered Mersenne numbers:", b11)
    print("Count of filtered Mersenne numbers:", len(b11))
    print("Lucas-Lehmer test results:")
    b12 = fonk3(3, 65)
    b13 = [(prime, fonk4(prime)) for prime in b12]
    print(b13)
    print("Fast prime check results:")
    for n in range(10000):
        assert fonk2(n) == fonk5(n)
    print("Get b9 fast:", fonk6(20))
    print("Sieve of Eratosthenes results match traditional prime list up to 1000:")
    assert fonk11(1000) == fonk3(0, 1000)