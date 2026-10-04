from collections import defaultdict
from heapq import *
def fonk1(edges, f, t):
    b1 = defaultdict(list)
    for l,r,c in edges:
        b1[l].append((c,r))
    q, b2 = [(0,f,())], set()
    while q:
        (cost,b4,b3) = heappop(q)
        if b4 not in b2:
            b2.add(b4)
            b3 = (b4, b3)
            if b4 = = t: return (cost, b3)
            for c, v2 in b1.get(b4, ()):
                if v2 not in b2:
                    heappush(q, (cost+c, v2, b3))
    return float("inf")