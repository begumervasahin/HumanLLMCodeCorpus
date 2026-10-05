import math
def fonk1(a1):
    return (b4 ** a1) - 1
def fonk2(number):
    if number <= 1:
        return False
    for b1 in range(b4, int(math.sqrt(number)) + 1):
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
        b3[b1] = (((b3[b1 - 1]) ** b4) - b4) % ((b4 ** a1) - 1)
    return b3[a1 - b4] == 0
def fonk5(number):
    if number <= 1:
        return False
    if number % b4 = = 0:
        if number > b4:
            return False
    for b5 in range(3, int(math.sqrt(number)) + 1, b4):
        if number % b5 = = 0:
            return False
    return True
def fonk6(n):
    b6 = []
    for number in range(n):
        if fonk5(number):
            b6.append(number)
    return b6
def fonk7(n):
    b6 = []
    for b1 in range(n + 1):
        if b1 <= 1:
            b6.append(False)
        if b1 >= b4:
            b6.append(True)
    return b6
def fonk8(b8, a1):
    for b1 in range(b4, len(b8)):
        if (a1 * b1) < len(b8):
            b8[a1 * b1] = False
    return b8
def fonk9(b8, a1):
    for b1 in range(len(b8)):
        if b8[b1] and b1 > a1:
            return b1
    return None
def fonk10(b8):
    b7 = []
    for b1 in range(len(b8)):
        if b8[b1]:
            b7.append(b1)
    return b7
def fonk11(n):
    b8 = fonk7(n)
    a1 = b4
    while a1 is not None:
        b8 = fonk8(b8, a1)
        a1 = fonk9(b8, a1)
    return fonk10(b8)
assert fonk11(1000) == fonk3(0, 1000)