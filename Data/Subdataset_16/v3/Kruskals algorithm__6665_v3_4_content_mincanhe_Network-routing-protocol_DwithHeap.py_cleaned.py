from collections import defaultdict
from heapq import heappush, heappop
def fonk1(b8, start, target):
    b1 = defaultdict(list)
    for from_node, to_node, cost in b8:
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
    return float("inf"), ()
def fonk2(b6):
    b4 = []
    while b6:
        b4.append(b6[0])
        b6 = b6[1]
    return b4[::-1]
if b7 = = "__main__":
    b8 = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3),
    ]
    b9 = 'A'
    b10 = 'E'
    cost, b4 = fonk1(b8, b9, b10)
    print(f"Shortest b4 from {b9} to {b10}:")
    print(f"Cost: {cost}")
    print(f"Path: {fonk2(b4)}")