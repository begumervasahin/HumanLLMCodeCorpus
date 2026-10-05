from collections import defaultdict
from heapq import *
def fonk1(b5, f, t):
    b1 = defaultdict(list)
    for l, r, c in b5:
        b1[l].append((c, r))
    q, b2 = [(0, f, ())], set()
    while q:
        (cost, b4, b3) = heappop(q)
        if b4 not in b2:
            b2.add(b4)
            b3 = (b4, b3)
            if b4 = = t:
                return (cost, b3)
            for c, v2 in b1.get(b4, ()):
                if v2 not in b2:
                    heappush(q, (cost + c, v2, b3))
    return float("inf")
b5 = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('B', 'D', 5),
    ('C', 'D', 1)
]
b6 = 'A'
b7 = 'D'
cost, b3 = fonk1(b5, b6, b7)
if cost != float("inf"):
    print("Shortest b3 from {} to {}: b8 = {}".format(b6, b7, cost))
    print("Path:", ' -> '.join(b3[0]), "=", b3[1])
else:
    print("There is no b3 from {} to {}.".format(b6, b7))