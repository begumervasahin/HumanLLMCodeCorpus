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
def fonk3(a, b):
    b2 = []
    for j in range(a, b):
        if fonk2(j):
            b2.append(j)
    return b2
def fonk4(a1):
    b3 = [4] * (a1 - 1)
    for b1 in range(1, a1 - 1):
        b3[b1] = (((b3[b1 - 1]) ** 2) - 2) % ((2 ** a1) - 1)
    if b3[a1 - 2] == 0:
        return 1
    else:
        return 0
def fonk5(n):
    b4 = []
    for number in range(n):
        if fonk2(number):
            b4.append(number)
    return b4
def fonk6(n):
    b4 = []
    for b1 in range(n + 1):
        if b1 <= 1:
            b4.append(False)
        if b1 >= 2:
            b4.append(True)
    return b4
def fonk7(b6, a1):
    for b1 in range(2, len(b6)):
        if (a1 * b1) < len(b6):
            b6[a1 * b1] = False
    return b6
def fonk8(b6, a1):
    for b1 in range(len(b6)):
        if (b6[b1] == True) and b1 > a1:
            return b1
def fonk9(b6):
    b5 = []
    for b1 in range(len(b6)):
        if b6[b1] == True:
            b5.append(b1)
    return b5
def fonk10(n):
    b6 = fonk6(n)
    a1 = 2
    while a1 is not None:
        b6 = fonk7(b6, a1)
        a1 = fonk8(b6, a1)
    return fonk9(b6)
print("Mersenne numbers:")
b7 = fonk3(3, 65)
b8 = [fonk1(prime) for prime in b7]
print(b8)
print(len(b8))
print("\nLucas-Lehmer test for primality:")
b9 = fonk3(3, 65)
b10 = [fonk4(idx) for idx in b9]
print(list(zip(b9, b10)))
print("\nSieve of Eratosthenes:")
print(fonk10(1000))