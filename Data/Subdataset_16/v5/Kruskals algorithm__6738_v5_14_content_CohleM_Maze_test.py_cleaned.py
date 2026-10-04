import random
from collections import defaultdict
def fonk1(b1 = 9):
    b2 = defaultdict(list)
    b3 = []
    a1 = 0
    for x in range(b1):
        for y in range(b1):
            b2[a1].append((x, y))
            a1 += 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if abs(dx) == abs(dy):
                        continue
                    b4 = (x + dx, y + dy)
                    if 0 <= b4[0] < b1 and 0 <= b4[1] < b1:
                        b5 = tuple(sorted([(x, y), b4]))
                        if b5 not in b3:
                            b3.append(b5)
    return b2, b3
def fonk2(b2, node):
    for tree_id, nodes in b2.items():
        if node in nodes:
            return tree_id, nodes
    return None, None
def fonk3(b2, b10, tree2_id):
    b2[b10].extend(b2[tree2_id])
    b2.pop(tree2_id)
def fonk4():
    b2, b3 = fonk1(b1=9)
    while len(b2) > 1:
        b6 = random.randint(0, len(b3) - 1)
        b7 = b3[b6]
        b10, b8 = fonk2(b2, b7[0])
        tree2_id, b9 = fonk2(b2, b7[1])
        if b10 = = tree2_id:
            continue
        print(f"Connecting b5: {b7}")
        print(f"Tree {b10} before merge: {b8}")
        print(f"Tree {tree2_id} before merge: {b9}")
        fonk3(b2, b10, tree2_id)
        b3.pop(b6)
        for tree_nodes in b2.values():
            print(tree_nodes)
        print(f"Remaining b3: {len(b3)}, Remaining trees: {len(b2)}")
        print()
    for tree_id, nodes in b2.items():
        print(f"Tree {tree_id}: {nodes}")
if b11 = = "__main__":
    fonk4()