from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(b10):
    b1 = len(b10)
    b2 = set()
    b3 = next(iter(b10))
    b2.add(b3)
    b4 = list(b10[b3])
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
        for edge in b10[b8]:
            if edge[1] not in b2:
                heappush(b5, edge)
    return b6, a1
b9 = open('edges.txt')
b10 = defaultdict(set)
next(b9)
for line in b9:
    b11 = line.split()
    b10[b11[0]].add((int(b11[2]), b11[1]))
    b10[b11[1]].add((int(b11[2]), b11[0]))
print(fonk1(b10))