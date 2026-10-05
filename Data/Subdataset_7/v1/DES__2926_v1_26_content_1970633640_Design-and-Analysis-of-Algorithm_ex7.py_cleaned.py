import random
from math import sqrt
a1 = 10000
b1 = list(range(a1))
random.shuffle(b1)
b2 = [-1] * a1
for b4 in range(a1 - 1):
    b2[b1[b4]] = b1[b4 + 1]
b3 = b1[0]
def fonk1(x, b4):
    a2 = 0
    while x > b1[b4]:
        b4 = b2[b4]
        a2 += 1
    return b4, a2
def fonk2(x):
    return fonk1(x, b3)
def fonk3(x):
    b4 = b3
    b5 = b1[b4]
    for j in range(int(sqrt(a1))):
        b6 = b1[j]
        if b5 < b6 <= x:
            b4 = j
            b5 = b6
    return fonk1(x, b4)
def fonk4(x):
    b4 = b3
    b5 = b1[b4]
    for _ in range(int(sqrt(a1))):
        b7 = random.randint(0, a1 - 1)
        b6 = b1[b7]
        if b5 < b6 <= x:
            b4 = b7
            b5 = b6
    return fonk1(x, b4)
def fonk5(x):
    b4 = random.randint(0, a1 - 1)
    b6 = b1[b4]
    if x < b6:
        return fonk1(x, b3)
    elif x > b6:
        return fonk1(x, b2[b4])
    else:
        return b4, 0
b8 = [fonk2(random.randint(0, a1 - 1))[1] for _ in range(100)]
b9 = [fonk3(random.randint(0, a1 - 1))[1] for _ in range(100)]
b10 = [fonk4(random.randint(0, a1 - 1))[1] for _ in range(100)]
b11 = [fonk5(random.randint(0, a1 - 1))[1] for _ in range(100)]
print(sum(b8) / len(b8))
print(sum(b9) / len(b9))
print(sum(b10) / len(b10))
print(sum(b11) / len(b11))