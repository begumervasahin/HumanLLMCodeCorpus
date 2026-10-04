import random
from collections import defaultdict
b1 = []
b2 = defaultdict(list)
a1 = 0
for x in range(9):
    for y in range(9):
        b2[a1].append((x, y))
        a1 += 1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if abs(dx) == abs(dy):
                    continue
                b3 = (x + dx, y + dy)
                if 0 <= b3[0] <= 8 and 0 <= b3[1] <= 8:
                    if [b3, (x, y)] in b1:
                        continue
                    b1.append([(x, y), b3])
b4 = []
while len(b2) > 1:
    b5 = random.randint(0, len(b1) - 1)
    b7, b6 = None, None
    for tree_id, nodes in b2.items():
        if b1[b5][0] in nodes:
            b7 = (tree_id, nodes)
        if b1[b5][1] in nodes:
            b6 = (tree_id, nodes)
        if b7 and b6:
            break
    if b7[0] == b6[0]:
        continue
    print(f"Connecting edge: {b1[b5]}")
    print(f"Before merging, b7: {b7[1]}")
    print(f"Before merging, b6: {b6[1]}")
    b7[1].extend(b6[1])
    b2.pop(b6[0])
    b1.pop(b5)
    b4.append(b5)
    for nodes in b2.values():
        print(nodes)
    print(f"Remaining b1: {len(b1)}, Remaining trees: {len(b2)}, Selected edge index: {b5}")
    print()
for tree_id, nodes in b2.items():
    print(f"Tree {tree_id}: {nodes}")