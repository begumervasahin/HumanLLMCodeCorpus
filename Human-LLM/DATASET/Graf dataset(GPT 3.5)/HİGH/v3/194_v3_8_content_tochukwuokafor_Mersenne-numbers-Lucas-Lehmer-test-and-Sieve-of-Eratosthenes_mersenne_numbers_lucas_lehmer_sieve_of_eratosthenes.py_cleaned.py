import math
def fonk1(a1):
    return (2 ** a1) - 1
def fonk2(number):
    if number <= 1:
        return False
    for b1 in range(2, int(math.sqrt(number)) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk3(start, end):
    b2 = []
    for num in range(start, end):
        if fonk2(num):
            b2.append(num)
    return b2
def fonk4(a1):
    b3 = [4] * (a1 - 1)
    for b1 in range(1, a1 - 1):
        b3[b1] = ((b3[b1 - 1] ** 2) - 2) % fonk1(a1)
    return b3[a1 - 2] == 0
def fonk5(n):
    b4 = [False, False] + [True] * (n - 1)
    a1 = 2
    while a1 is not None:
        for b1 in range(2 * a1, n + 1, a1):
            b4[b1] = False
        a1 = next((b1 for b1 in range(a1 + 1, n + 1) if b4[b1]), None)
    return [b1 for b1, prime in enumerate(b4) if prime]
print("Mersenne numbers:")
b5 = fonk3(3, 65)
b6 = [fonk1(prime) for prime in b5]
print(b6)
print(len(b6))
print("\nLucas-Lehmer test for primality:")
b7 = fonk3(3, 65)
b8 = [fonk4(prime) for prime in b7]
print(list(zip(b7, b8)))
print("\nSieve of Eratosthenes:")
print(fonk5(1000))