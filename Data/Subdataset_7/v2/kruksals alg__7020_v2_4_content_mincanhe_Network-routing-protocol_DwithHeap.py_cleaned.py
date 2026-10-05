from collections import defaultdict
from heapq import heappop, heappush
def fonk1(b5, start, end):
    b1 = defaultdict(list)
    for b6, b7, cost in b5:
        b1[b6].append((cost, b7))
    queue, b2 = [(0, start, ())], set()
    while queue:
        (current_cost, b4, b3) = heappop(queue)
        if b4 not in b2:
            b2.add(b4)
            b3 = (b4, b3)
            if b4 = = end:
                return (current_cost, b3)
            for cost, next_node in b1.get(b4, ()):
                if next_node not in b2:
                    heappush(queue, (current_cost + cost, next_node, b3))
    return float("inf"), None
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
    print(f"Shortest b3 from {b6} to {b7}: b8 = {cost}")
    print("Path:", ' -> '.join(b3[0]), "=", b3[1])
else:
    print(f"There is no b3 from {b6} to {b7}.")