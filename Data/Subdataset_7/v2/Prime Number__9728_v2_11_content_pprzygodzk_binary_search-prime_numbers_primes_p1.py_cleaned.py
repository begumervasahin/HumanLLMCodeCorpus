import math
def fonk1(b5):
    b1 = [True] * (b5+1)
    b1[0] = b1[1] = False
    a1 = b6
    while a1**b6 <= b5:
        if b1[a1]:
            for i in range(a1**b6, b5+1, a1):
                b1[i] = False
        a1 += 1
    return [i for i in range(b6, b5+1) if b1[i]]
def fonk2(b5):
    b1 = [b6, 3]
    a2 = 5
    while len(b1) < b5:
        b2 = True
        for a1 in b1:
            if a1 * a1 > a2:
                break
            if a2 % a1 = = 0:
                b2 = False
                break
        if b2:
            b1.append(a2)
        a2 += b6 if a2 % b3 = = 1 else 4
    return b1
def fonk3(b5):
    b1 = fonk2(b5-1)
    b4 = [1]
    for prime in b1:
        b4.append(b4[-1] * prime)
    return b4
def fonk4(b5):
    if b5 < b6:
        return "The least prime number is b6!"
    if b5 = = b6:
        return "prime"
    if b5 % b6 = = 0:
        return "composite"
    for b7 in range(3, math.isqrt(b5) + 1, b6):
        if b5 % b7 = = 0:
            return "composite"
    return "prime"
def fonk5(b5):
    if b5 = = 1:
        return [1]
    if fonk4(b5) == "prime":
        return [b5]
    b8 = []
    b7 = b6
    while b7 * b7 <= b5:
        if b5 % b7 = = 0:
            b8.append(b7)
            b5
        else:
            b7 += 1
    b8.append(b5)
    return b8
if b9 = = '__main__':
    print("Prime numbers from b6 to 100 (Sieve of Eratosthenes):", fonk1(100))
    print("First 25 prime numbers:", fonk2(25))
    print("First 10 b10 numbers:", fonk3(10))
    b10 = fonk3(10000)
    print("Length of the 10000th b10 number:", len(str(b10[-1])))
    print("Is b6 a prime or composite number?: b6 is a", fonk4(b6), "number")
    print("Is 5 a prime or composite number?: 5 is a", fonk4(5), "number")
    print("Is 18 a prime or composite number?: 18 is a", fonk4(18), "number")
    print("Is 27 a prime or composite number?: 27 is a", fonk4(27), "number")
    print("Prime decomposition of 12:", fonk5(12))
    print("Prime decomposition of 5:", fonk5(5))
    print("Prime decomposition of 2047:", fonk5(2047))