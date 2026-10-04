import random
from collections import defaultdict
b1 = []
b2 = defaultdict(list)
a1 = 0
for b5 in range(9):
    for b in range(9):
        b2[a1].append((b5, b))
        a1 += 1
        for b7 in range(-1, 2):
            for d in range(-1, 2):
                if abs(b7) == abs(d):
                    continue
                b3 = (b5 + b7, b + d)
                if 0 <= b3[0] <= 8 and 0 <= b3[1] <= 8:
                    if [b3, (b5, b)] in b1:
                        continue
                    b1.append([(b5, b), b3])
b4 = []
while len(b2) > 1:
    b5 = random.randint(0, len(b1) - 1)
    b6 = b9 = None
    for b in b2:
        for b7 in b2[b]:
            if b7 = = b1[b5][0]:
                b6 = (b, b7)
                break
        if b6:
            break
    for d in b2:
        for b8 in b2[d]:
            if b8 = = b1[b5][1]:
                b9 = (d, b8, b2[d])
                break
        if b9:
            break
    if b6[0] == b9[0]:
        continue
    print(f"Connecting edge: {b1[b5]}")
    print(f"b6[0]: {b2[b6[0]]}")
    print(f"b9[2]: {b9[2]}")
    b2[b6[0]].extend(b9[2])
    b2.pop(b9[0], None)
    b1.pop(b5)
    b4.append(b5)
    for k in b2:
        print(b2[k])
    print(f"Remaining b1: {len(b1)}, Remaining trees: {len(b2)}, Chosen edge index: {b5}")
    print('\n')
for key, value in b2.items():
    print(f"{key}: {value}")