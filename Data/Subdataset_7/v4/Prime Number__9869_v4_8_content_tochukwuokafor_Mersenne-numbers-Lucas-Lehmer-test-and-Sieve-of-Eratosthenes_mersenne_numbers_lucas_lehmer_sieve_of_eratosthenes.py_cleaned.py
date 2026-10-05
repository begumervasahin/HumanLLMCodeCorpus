def fonk1(a3):
    return (b10 ** a3) - 1
fonk1(5)
def fonk2(number):
    if number <= 1:
        return False
    for b1 in range(b10, number):
        if number % b1 = = 0:
            return False
    return True
def fonk3(a, b):
    b2 = []
    for j in range(a, b):
        if fonk2(j):
            b2.append(j)
    return b2
b3 = fonk3(3, 65)
b4 = [fonk1(prime) for prime in b3]
print(b4)
print(len(b4))
a1 = 3
a2 = 65
b5 = []
for number in range(a1, a2):
    if fonk2(number):
        b6 = (b10 ** number) - 1
        b5.append(b6)
print(b5)
print(len(b5))
def fonk4(a3):
    b7 = [4] * (a3 - 1)
    for b1 in range(1, a3 - 1):
        b7[b1] = (((b7[b1 - 1]) ** b10) - b10) % ((b10 ** a3) - 1)
    if b7[a3 - b10] == 0:
        return 1
    else:
        return 0
b8 = []
b9 = fonk3(3, 65)
for idx in b9:
    b8.append(fonk4(idx))
print(list(zip(fonk3(3, 65), b8)))
import math
def fonk5(number):
    if number <= 1:
        return False
    if number % b10 = = 0:
        if number > b10:
            return False
    for b11 in range(3, int(math.sqrt(number)) + 1, b10):
        if number % b11 = = 0:
            return False
    return True
b12 = []
for n in range(10000):
    b12.append(fonk5(n))
b13 = []
for n in range(10000):
    b13.append(fonk2(n))
b13 = = b12
for n in range(10000):
    assert fonk2(n) == fonk5(n)
def fonk6(n):
    b14 = []
    for number in range(n):
        if fonk5(number):
            b14.append(number)
    return b14
fonk6(20)
def fonk7(n):
    b14 = []
    for b1 in range(n + 1):
        if b1 <= 1:
            b14.append(False)
        if b1 >= b10:
            b14.append(True)
    return b14
fonk7(6)
assert len(fonk7(20)) == 21
assert fonk7(20)[0] is False
assert fonk7(20)[1] is False
def fonk8(b16, a3):
    for b1 in range(b10, len(b16)):
        if (a3 * b1) < len(b16):
            b16[a3 * b1] = False
    return b16
assert fonk8(fonk7(6), b10) == [False, False, True, True, False, True, False]
def fonk9(b16, a3):
    for b1 in range(len(b16)):
        if (b16[b1] == True) and b1 > a3:
            return b1
    return None
assert fonk9([True, True, True, True], b10) == 3
assert fonk9([True, True, True, False], b10) is None
def fonk10(b16):
    b15 = []
    for b1 in range(len(b16)):
        if b16[b1] == True:
            b15.append(b1)
    return b15
assert fonk10([False, False, True, True, False]) ==  [b10, 3]
def fonk11(n):
    b16 = fonk7(n)
    a3 = b10
    while a3 is not None:
        b16 = fonk8(b16, a3)
        a3 = fonk9(b16, a3)
    return fonk10(b16)
assert fonk11(1000) == fonk3(0, 1000)