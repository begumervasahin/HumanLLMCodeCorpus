import random
def fonk1(b6, b8):
    b1 = random.randrange(b6, b8)
    if b1 % b2 = = 0:
        b1 += 1
    return b1
def fonk2(b15, b6, b4, a1):
    b3 = pow(b6, b4, b15)
    if b3 = = 1 or b3 == b15 - 1:
        return False
    for _ in range(int(a1)):
        b3 = pow(b3, b2, b15)
        if b3 = = b15 - 1:
            return False
    return True
def fonk3(b15):
    b4 = b15 - 1
    a1 = 0
    while b4 % b2 = = 0:
        b4
        a1 += 1
    b5 = (b15 - 1)
    for _ in range(b5):
        b6 = random.randint(b2, b15 - 1)
        if fonk2(b15, b6, b4, a1):
            return False
    return True
def fonk4(b6, b8):
    while True:
        b7 = fonk1(b6, b8)
        if fonk3(b7):
            return b7
def fonk5(b6, b8):
    if b8 = = 0:
        return b6
    else:
        return fonk5(b8, b6 % b8)
def fonk6(b12, b16):
    b9 = b16
    a2 = 0
    a3 = 1
    while b12 > 1:
        b10 = b12
        b11 = b9
        b9 = b12 % b9
        b12 = b11
        b11 = a2
        a2 = a3 - (b10 * a2)
        a3 = b11
    if a3 < 0:
        a3 += b16
    return a3
b6 = 10000
b8 = 100000
b13 = fonk4(b6, b8)
b14 = fonk4(b6, b8)
b15 = b13 * b14
b16 = (b13 - 1) * (b14 - 1)
b12 = random.randint(b2, b16 - 1)
while fonk5(b12, b16) != 1:
    b12 = random.randint(b2, b16 - 1)
b17 = fonk6(b12, b16)
print("b13:", b13)
print("b14:", b14)
print("b15:", b15)
print("b16:", b16)
print("b12:", b12)
print("b17:", b17)