import random
from collections import defaultdict
edges = []
tree = defaultdict(list)
count = 0
for a in range(9):
    for b in range(9):
        tree[count].append((a, b))
        count += 1
        for c in range(-1, 2):
            for d in range(-1, 2):
                if abs(c) == abs(d):
                    continue
                flag = (a + c, b + d)
                if 0 <= flag[0] <= 8 and 0 <= flag[1] <= 8:
                    if [flag, (a, b)] in edges:
                        continue
                    edges.append([(a, b), flag])
rand_nums = []
while len(tree) > 1:
    a = random.randint(0, len(edges) - 1)
    t1 = t2 = None
    for b in tree:
        for c in tree[b]:
            if c == edges[a][0]:
                t1 = (b, c)
                break
        if t1:
            break
    for d in tree:
        for e in tree[d]:
            if e == edges[a][1]:
                t2 = (d, e, tree[d])
                break
        if t2:
            break
    if t1[0] == t2[0]:
        continue
    print(f"Connecting edge: {edges[a]}")
    print(f"t1[0]: {tree[t1[0]]}")
    print(f"t2[2]: {t2[2]}")
    tree[t1[0]].extend(t2[2])
    tree.pop(t2[0], None)
    edges.pop(a)
    rand_nums.append(a)
    for k in tree:
        print(tree[k])
    print(f"Remaining edges: {len(edges)}, Remaining trees: {len(tree)}, Chosen edge index: {a}")
    print('\n')
for key, value in tree.items():
    print(f"{key}: {value}")