import random
from math import sqrt
a1 = 10000
b1 = list(range(a1))
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
random.shuffle(b1)
for b8 in range(a1):
    if b8 != a1 - 1:
        b2.append(b1.index(b8 + 1))
    else:
        b2.append(-1)
b7 = b1.index(0)
def fonk1(b12, b8):
    a2 = 0
    while b12 > b1[b8]:
        b8 = b2[b8]
        a2 += 1
    return b8, a2
def fonk2(b12):
    return fonk1(b12, b7)
def fonk3(b12):
    b8 = b7
    b9 = b1[b8]
    for j in range(int(sqrt(a1))):
        b10 = b1[j]
        if b9 < b10 <= b12:
            b8 = j
            b9 = b10
    return fonk1(b12, b8)
def fonk4(b12):
    b8 = b7
    b9 = b1[b8]
    for _ in range(int(sqrt(a1))):
        b11 = random.randint(0, a1 - 1)
        b10 = b1[b11]
        if b9 < b10 <= b12:
            b8 = b11
            b9 = b10
    return fonk1(b12, b8)
def fonk5(b12):
    b8 = random.randint(0, a1 - 1)
    b10 = b1[b8]
    if b12 < b10:
        return fonk1(b12, b7)
    elif b12 > b10:
        return fonk1(b12, b2[b8])
    else:
        return b8, 0
for _ in range(100):
    b12 = random.randint(0, a1 - 1)
    b3.append(fonk2(b12)[1])
    b4.append(fonk3(b12)[1])
    b5.append(fonk4(b12)[1])
    b6.append(fonk5(b12)[1])
print("Average Search Count Type A:", sum(b3) / len(b3))
print("Average Search Count Type B:", sum(b4) / len(b4))
print("Average Search Count Type C:", sum(b5) / len(b5))
print("Average Search Count Type D:", sum(b6) / len(b6))