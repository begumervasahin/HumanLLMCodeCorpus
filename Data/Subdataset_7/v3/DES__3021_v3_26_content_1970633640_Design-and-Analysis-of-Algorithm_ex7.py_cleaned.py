import random
from math import sqrt
a1 = 10000
b1 = list(range(a1))
random.shuffle(b1)
b2 = [-1] * a1
for i in range(a1 - 1):
    b2[b1[i]] = b1[i + 1]
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
        b8 = b1[b7]
        if b5 < b8 <= x:
            b4 = b7
            b5 = b8
    return fonk1(x, b4)
def fonk5(x):
    b7 = random.randint(0, a1 - 1)
    b8 = b1[b7]
    if x < b8:
        return fonk1(x, b3)
    elif x > b8:
        return fonk1(x, b2[b7])
    else:
        return b7, 0
b9 = [fonk2(random.randint(0, a1 - 1))[1] for _ in range(100)]
b10 = [fonk3(random.randint(0, a1 - 1))[1] for _ in range(100)]
b11 = [fonk4(random.randint(0, a1 - 1))[1] for _ in range(100)]
b12 = [fonk5(random.randint(0, a1 - 1))[1] for _ in range(100)]
print("Average Steps Type A:", sum(b9) / len(b9))
print("Average Steps Type B:", sum(b10) / len(b10))
print("Average Steps Type C:", sum(b11) / len(b11))
print("Average Steps Type D:", sum(b12) / len(b12))