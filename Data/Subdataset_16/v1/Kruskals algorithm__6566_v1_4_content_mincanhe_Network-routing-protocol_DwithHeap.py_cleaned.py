from collections import defaultdict
from heapq import heappush, heappop
def fonk1(b8, start, target):
    b1 = defaultdict(list)
    for left, right, cost in b8:
        b1[left].append((cost, right))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        (cost, b5, b4) = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = target:
                return (cost, b4)
            for neighbor_cost, neighbor in b1.get(b5, ()):
                if neighbor not in b3:
                    heappush(b2, (cost + neighbor_cost, neighbor, b4))
    return float("inf")
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
    print("Shortest b4 from {} to {}:".format(b9, b10))
    print("Cost:", cost)
    print("Path:", fonk2(b4))