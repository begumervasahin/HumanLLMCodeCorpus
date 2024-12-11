import random
from math import sqrt
a1 = 10000
b1 = []
b2 = []
a2 = 0
b3 = []
b4 = []
b5 = []
b6 = []
for b7 in range(0, a1):
    b1.append(b7)
random.shuffle(b1)
for b7 in b1:
    if b7 != a1 - 1:
        b2.append(b1.index(b7 + 1))
    else:
        b2.append(-1)
a2 = b1.index(0)
def fonk1(b11, b7):
    a3 = 0
    while b11 > b1[b7]:
        b7 = b2[b7]
        a3 += 1
    return b7, a3
def fonk2(b11):
    return fonk1(b11, a2)
def fonk3(b11):
    b7 = a2
    b8 = b1[b7]
    for j in range(0, int(sqrt(a1))):
        b9 = b1[j]
        if b8 < b9 <= b11:
            b7 = j
            b8 = b9
    return fonk1(b11, b7)
def fonk4(b11):
    b7 = a2
    b8 = b1[b7]
    for j in range(0, int(sqrt(a1))):
        b10 = random.randint(0, a1 - 1)
        b9 = b1[b10]
        if b8 < b9 <= b11:
            b7 = b10
            b8 = b9
    return fonk1(b11, b7)
def fonk5(b11):
    a3 = 0
    b7 = random.randint(0, a1 - 1)
    b9 = b1[b7]
    if b11 < b9:
        return fonk1(b11, a2)
    elif b11 > b9:
        return fonk1(b11, b2[b7])
    else:
        return b7, 0
for b7 in range(100):
    b11 = random.randint(0, a1 - 1)
    b3.append(fonk2(b11)[1])
    b4.append(fonk3(b11)[1])
    b5.append(fonk4(b11)[1])
    b6.append(fonk5(b11)[1])
print(sum(b3) / len(b3))
print(sum(b4) / len(b4))
print(sum(b5) / len(b5))
print(sum(b6) / len(b6))