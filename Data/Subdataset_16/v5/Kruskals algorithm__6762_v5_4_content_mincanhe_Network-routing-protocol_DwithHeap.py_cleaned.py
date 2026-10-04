from collections import defaultdict
from heapq import heappop, heappush
def fonk1(edges, start, target):
    b1 = defaultdict(list)
    for from_node, to_node, cost in edges:
        b1[from_node].append((cost, to_node))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        current_cost, b5, b4 = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = target:
                return current_cost, b4
            for neighbor_cost, neighbor in b1[b5]:
                if neighbor not in b3:
                    heappush(b2, (current_cost + neighbor_cost, neighbor, b4))
    return float("inf"), None
def fonk2(b4):
    b6 = []
    while b4:
        node, b4 = b4
        b6.append(node)
    return b6[::-1]
