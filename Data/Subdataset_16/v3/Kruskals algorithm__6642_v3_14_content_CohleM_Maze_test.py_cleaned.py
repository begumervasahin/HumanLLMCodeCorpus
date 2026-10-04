import random
from collections import defaultdict
def fonk1(b1 = 9):
    b2 = []
    b3 = defaultdict(list)
    a1 = 0
    for x in range(b1):
        for y in range(b1):
            b3[a1].append((x, y))
            a1 += 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if abs(dx) == abs(dy):
                        continue
                    b4 = (x + dx, y + dy)
                    if 0 <= b4[0] < b1 and 0 <= b4[1] < b1:
                        b5 = sorted([(x, y), b4])
                        if b5 not in b2:
                            b2.append(b5)
    return b3, b2
def fonk2(b3, b5):
    b7, b6 = None, None
    for tree_id, nodes in b3.items():
        if b5[0] in nodes:
            b7 = tree_id
        if b5[1] in nodes:
            b6 = tree_id
        if b7 is not None and b6 is not None:
            break
    return b7, b6
def fonk3(b3, b11, b10):
    b3[b11].extend(b3[b10])
    b3.pop(b10)
def fonk4():
    b3, b2 = fonk1(b1=9)
    while len(b3) > 1:
        b8 = random.randint(0, len(b2) - 1)
        b9 = b2[b8]
        b11, b10 = fonk2(b3, b9)
        if b11 = = b10:
            continue
        print(f"Connecting b5: {b9}")
        print(f"Before merging, b3 {b11}: {b3[b11]}")
        print(f"Before merging, b3 {b10}: {b3[b10]}")
        fonk3(b3, b11, b10)
        b2.pop(b8)
        print(f"Remaining b2: {len(b2)}, Remaining trees: {len(b3)}")
        print()
    for tree_id, nodes in b3.items():
        print(f"Tree {tree_id}: {nodes}")
if b12 = = "__main__":
    fonk4()