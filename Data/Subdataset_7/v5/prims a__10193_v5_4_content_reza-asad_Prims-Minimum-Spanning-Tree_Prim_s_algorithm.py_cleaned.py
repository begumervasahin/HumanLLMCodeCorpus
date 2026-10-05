from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(b8):
    b1 = len(b8)
    b2 = set()
    b3 = next(iter(b8))
    b2.add(b3)
    b4 = list(b8[b3])
    heapify(b4)
    b5 = [b3]
    a1 = 0
    while len(b5) != b1:
        b9, b6 = heappop(b4)
        if b6 in b2:
            continue
        a1 += b9
        b5.append(b6)
        b2.add(b6)
        for neighbor_weight, neighbor_vertex in b8[b6]:
            if neighbor_vertex not in b2:
                heappush(b4, (neighbor_weight, neighbor_vertex))
    return b5, a1
b7 = open('edges.txt')
b8 = defaultdict(set)
next(b7)
for line in b7:
    vertex1, vertex2, b9 = line.split()
    b9 = int(b9)
    b8[vertex1].add((b9, vertex2))
    b8[vertex2].add((b9, vertex1))
print(fonk1(b8))