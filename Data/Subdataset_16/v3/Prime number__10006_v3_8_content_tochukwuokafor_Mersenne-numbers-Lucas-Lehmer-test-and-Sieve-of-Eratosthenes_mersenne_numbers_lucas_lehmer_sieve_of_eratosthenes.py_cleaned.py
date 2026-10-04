import math
def fonk1(a1):
    return (b5 ** a1) - 1
def fonk2(b4):
    if b4 <= 1:
        return False
    for b1 in range(b5, int(math.sqrt(b4)) + 1):
        if b4 % b1 = = 0:
            return False
    return True
def fonk3(a, b):
    return [j for j in range(a, b) if fonk2(j)]
def fonk4(a1):
    b2 = [4]
    b3 = fonk1(a1)
    for _ in range(1, a1 - 1):
        b2.append((b2[-1] ** b5 - b5) % b3)
    return b2
def fonk5(a1):
    return fonk4(a1)[-1] == 0
def fonk6(b4):
    if b4 <= 1:
        return False
    if b4 = = b5:
        return True
    if b4 % b5 = = 0:
        return False
    for b6 in range(3, int(math.sqrt(b4)) + 1, b5):
        if b4 % b6 = = 0:
            return False
    return True
def fonk7(n):
    return [b4 for b4 in range(n) if fonk6(b4)]
def fonk8(n):
    return [False, False] + [True] * (n - 1)
def fonk9(b7, a1):
    for b1 in range(a1 * b5, len(b7), a1):
        b7[b1] = False
    return b7
def fonk10(b7, a1):
    for b1 in range(a1 + 1, len(b7)):
        if b7[b1]:
            return b1
    return None
def fonk11(b7):
    return [b1 for b1, is_prime in enumerate(b7) if is_prime]
def fonk12(n):
    b7 = fonk8(n)
    a1 = b5
    while a1 is not None:
        b7 = fonk9(b7, a1)
        a1 = fonk10(b7, a1)
    return fonk11(b7)
if b8 = = '__main__':
    b9 = fonk3(3, 65)
    b10 = [fonk1(prime) for prime in b9]
    print("Mersenne numbers:", b10)
    print("Number of Mersenne numbers:", len(b10))
    print("Checked Mersenne numbers:", b10)
    print("Number of checked Mersenne numbers:", len(b10))
    b11 = [(a1, fonk5(a1)) for a1 in b9]
    print("Lucas-Lehmer test results:", b11)
    b12 = [fonk6(n) for n in range(10000)]
    b13 = [fonk2(n) for n in range(10000)]
    print("Fast and slow prime lists are identical:", b13 = = b12)
    b14 = fonk7(20)
    print("Primes up to 20:", b14)
    assert len(fonk8(20)) == 21
    assert fonk8(20)[0] is False
    assert fonk8(20)[1] is False
    assert fonk9(fonk8(6), b5) == [False, False, True, True, False, True, False]
    assert fonk10([True, True, True, True], b5) == 3
    assert fonk10([True, True, True, False], b5) is None
    assert fonk11([False, False, True, True, False]) == [b5, 3]
    assert fonk12(1000) == fonk3(0, 1000)
    print("All assertions passed successfully.")