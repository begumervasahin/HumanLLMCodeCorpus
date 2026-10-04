import math
def fonk1(a1):
    return (b3 ** a1) - 1
def fonk2(b4):
    if b4 <= 1:
        return False
    for b1 in range(b3, int(math.sqrt(b4)) + 1):
        if b4 % b1 = = 0:
            return False
    return True
def fonk3(a, b):
    return [j for j in range(a, b) if fonk2(j)]
def fonk4(a1):
    b2 = [4] * (a1 - 1)
    for b1 in range(1, a1 - 1):
        b2[b1] = (((b2[b1 - 1]) ** b3) - b3) % ((b3 ** a1) - 1)
    return b2
def fonk5(a1):
    b2 = fonk4(a1)
    return b2[-1] == 0
def fonk6(b4):
    if b4 <= 1:
        return False
    if b4 % b3 = = 0:
        return b4 = = b3
    for b5 in range(3, int(math.sqrt(b4)) + 1, b3):
        if b4 % b5 = = 0:
            return False
    return True
def fonk7(n):
    return [b4 for b4 in range(n) if fonk6(b4)]
def fonk8(n):
    return [False, False] + [True] * (n - 1)
def fonk9(b6, a1):
    for b1 in range(b3, len(b6)):
        if a1 * b1 < len(b6):
            b6[a1 * b1] = False
    return b6
def fonk10(b6, a1):
    for b1 in range(a1 + 1, len(b6)):
        if b6[b1]:
            return b1
    return None
def fonk11(b6):
    return [b1 for b1, is_prime in enumerate(b6) if is_prime]
def fonk12(n):
    b6 = fonk8(n)
    a1 = b3
    while a1 is not None:
        b6 = fonk9(b6, a1)
        a1 = fonk10(b6, a1)
    return fonk11(b6)
if b7 = = '__main__':
    b8 = fonk3(3, 65)
    b9 = [fonk1(prime) for prime in b8]
    print("Mersenne numbers:", b9)
    print("Number of Mersenne numbers:", len(b9))
    b10 = [fonk1(prime) for prime in fonk3(3, 65)]
    print("Checked Mersenne numbers:", b10)
    print("Number of checked Mersenne numbers:", len(b10))
    b11 = fonk3(3, 65)
    b12 = [fonk5(a1) for a1 in b11]
    print("Lucas-Lehmer test results:", list(zip(b11, b12)))
    b13 = [fonk6(n) for n in range(10000)]
    b14 = [fonk2(n) for n in range(10000)]
    print("Fast and slow prime lists are identical:", b14 = = b13)
    b15 = fonk7(20)
    print("Primes up to 20:", b15)
    assert len(fonk8(20)) == 21
    assert fonk8(20)[0] is False
    assert fonk8(20)[1] is False
    assert fonk9(fonk8(6), b3) == [False, False, True, True, False, True, False]
    assert fonk10([True, True, True, True], b3) == 3
    assert fonk10([True, True, True, False], b3) is None
    assert fonk11([False, False, True, True, False]) == [b3, 3]
    assert fonk12(1000) == fonk3(0, 1000)
    print("All assertions passed successfully.")