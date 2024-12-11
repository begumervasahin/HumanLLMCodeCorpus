import random
def fonk1(start, end):
    b1 = random.randrange(start, end)
    if b1 % b2 = = 0:
        b1 += 1
    return b1
def fonk2(b14, b6, b4, a1):
    b3 = pow(b6, b4, b14)
    if b3 = = 1 or b3 == b14 - 1:
        return False
    for _ in range(int(a1)):
        b3 = pow(b3, b2, b14)
        if b3 = = b14 - 1:
            return False
    return True
def fonk3(b14):
    b4 = b14 - 1
    a1 = 0
    while b4 % b2 = = 0:
        b4
        a1 += 1
    b5 = (b14 - 1)
    for _ in range(b5):
        b6 = random.randint(b2, b14 - 1)
        if fonk2(b14, b6, b4, a1):
            return False
    return True
def fonk4(start, end):
    while True:
        b7 = fonk1(start, end)
        if fonk3(b7):
            return b7
def fonk5(a, b8):
    while b8:
        a, b8 = b8, a % b8
    return a
def fonk6(b15, b11):
    x, b9 = 0, 1
    while b11:
        b10 = b15
        b15, b11 = b11, b15 % b11
        x, b9 = b9, x - b10 * b9
    return x % b11
a2 = 10000
a3 = 100000
b12 = fonk4(a2, a3)
b13 = fonk4(a2, a3)
b14 = b12 * b13
b11 = (b12 - 1) * (b13 - 1)
b15 = random.randint(b2, b11 - 1)
while fonk5(b15, b11) != 1:
    b15 = random.randint(b2, b11 - 1)
b16 = fonk6(b15, b11)
print("b12:", b12)
print("b13:", b13)
print("b14:", b14)
print("b11:", b11)
print("b15:", b15)
print("b16:", b16)