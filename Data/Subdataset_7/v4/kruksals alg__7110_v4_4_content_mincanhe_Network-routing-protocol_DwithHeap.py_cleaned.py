from collections import defaultdict
from heapq import heappop, heappush
def fonk1(edges, start, end):
    b1 = defaultdict(list)
    for left, right, cost in edges:
        b1[left].append((cost, right))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        cost, b5, b4 = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = end:
                return (cost, b4)
            for next_cost, next_vertex in b1.get(b5, ()):
                if next_vertex not in b3:
                    heappush(b2, (cost + next_cost, next_vertex, b4))
    return float("inf")