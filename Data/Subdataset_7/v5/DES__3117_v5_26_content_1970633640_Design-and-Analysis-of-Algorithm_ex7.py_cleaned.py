import random
from math import sqrt
a1 = 10000
b1 = list(range(a1))
b2 = []
b3 = {'A': [], 'B': [], 'C': [], 'D': []}
random.shuffle(b1)
for b5 in range(a1):
    if b5 != a1 - 1:
        b2.append(b1.index(b5 + 1))
    else:
        b2.append(-1)
b4 = b1.index(0)
def fonk1(b9, b5):
    a2 = 0
    while b9 > b1[b5]:
        b5 = b2[b5]
        a2 += 1
    return b5, a2
def fonk2(b9):
    return fonk1(b9, b4)
def fonk3(b9):
    b5 = b4
    b6 = b1[b5]
    for j in range(int(sqrt(a1))):
        b7 = b1[j]
        if b6 < b7 <= b9:
            b5 = j
            b6 = b7
    return fonk1(b9, b5)
def fonk4(b9):
    b5 = b4
    b6 = b1[b5]
    for _ in range(int(sqrt(a1))):
        b8 = random.randint(0, a1 - 1)
        b7 = b1[b8]
        if b6 < b7 <= b9:
            b5 = b8
            b6 = b7
    return fonk1(b9, b5)
def fonk5(b9):
    b5 = random.randint(0, a1 - 1)
    b7 = b1[b5]
    if b9 < b7:
        return fonk1(b9, b4)
    elif b9 > b7:
        return fonk1(b9, b2[b5])
    else:
        return b5, 0
for _ in range(100):
    b9 = random.randint(0, a1 - 1)
    for search_type in b3:
        b3[search_type].append(globals()[f"search_type_{search_type.lower()}"](b9)[1])
for search_type, counts in b3.items():
    b10 = sum(counts) / len(counts)
    print(f"Average Search Count Type {search_type}:", b10)