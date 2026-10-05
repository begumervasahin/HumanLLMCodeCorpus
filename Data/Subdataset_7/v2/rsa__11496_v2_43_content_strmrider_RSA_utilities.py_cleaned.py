import random
def fonk1(start, end):
    b1 = random.randrange(start, end)
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
def fonk4(start, end):
    while True:
        b7 = fonk1(start, end)
        if fonk3(b7):
            return b7
def fonk5(b6, b8):
    while b8:
        b6, b8 = b8, b6 % b8
    return b6
def fonk6(b12, b16):
    b9 = b16
    y, b10 = 0, 1
    while b12 > 1:
        b11 = b12
        b9, b12 = b12 % b9, b9
        y, b10 = b10 - b11 * y, y
    return b10 % b16
a2 = 10000
a3 = 100000
b13 = fonk4(a2, a3)
b14 = fonk4(a2, a3)
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