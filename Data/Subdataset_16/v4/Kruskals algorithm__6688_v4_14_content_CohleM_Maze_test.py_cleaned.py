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
def fonk2(b3, node):
    for tree_id, nodes in b3.items():
        if node in nodes:
            return tree_id, nodes
    return None, None
def fonk3(b3, b11, tree2_id):
    b3[b11].extend(b3[tree2_id])
    b3.pop(tree2_id)
def fonk4():
    b3, b2 = fonk1(b1=9)
    b6 = []
    while len(b3) > 1:
        b7 = random.randint(0, len(b2) - 1)
        b8 = b2[b7]
        b11, b9 = fonk2(b3, b8[0])
        tree2_id, b10 = fonk2(b3, b8[1])
        if b11 = = tree2_id:
            continue
        print(f"Connecting b5: {b8}")
        print(f"Tree {b11} before merge: {b9}")
        print(f"Tree {tree2_id} before merge: {b10}")
        fonk3(b3, b11, tree2_id)
        b2.pop(b7)
        b6.append(b7)
        for nodes in b3.values():
            print(nodes)
        print(f"Remaining b2: {len(b2)}, Remaining trees: {len(b3)}")
        print()
    for tree_id, nodes in b3.items():
        print(f"Tree {tree_id}: {nodes}")
if b12 = = "__main__":
    fonk4()