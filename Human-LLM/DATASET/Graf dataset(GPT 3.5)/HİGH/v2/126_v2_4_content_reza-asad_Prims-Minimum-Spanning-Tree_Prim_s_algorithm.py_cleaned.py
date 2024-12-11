from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(b9):
    b1 = len(b9)
    b2 = set()
    b3 = next(iter(b9.keys()))
    b2.add(b3)
    b4 = list(b9[b3])
    b5 = b4
    heapify(b5)
    b6 = [b3]
    a1 = 0
    while len(b6) != b1:
        b7 = heappop(b5)
        if b7[1] in b2:
            continue
        a1 += b7[0]
        b8 = b7[1]
        b6.append(b8)
        b2.add(b8)
        for edge in b9[b8]:
            if edge[1] not in b2:
                heappush(b5, edge)
    return b6, a1
def fonk2(filename):
    b9 = defaultdict(set)
    with open(filename, 'r') as data_file:
        next(data_file)
        for line in data_file:
            b10 = line.split()
            b9[b10[0]].add((int(b10[2]), b10[1]))
            b9[b10[1]].add((int(b10[2]), b10[0]))
    return b9
if b11 = = "__main__":
    b9 = fonk2('edges.txt')
    mst_nodes, a1 = fonk1(b9)
    print("Minimum Spanning Tree Nodes:", mst_nodes)
    print("Total Cost:", a1)