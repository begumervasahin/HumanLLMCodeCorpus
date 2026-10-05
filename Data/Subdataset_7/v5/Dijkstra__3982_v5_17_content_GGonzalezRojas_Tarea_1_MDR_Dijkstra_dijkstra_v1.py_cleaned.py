from collections import defaultdict
from heapq import heappop, heappush
def fonk1(b8, start, end):
    b1 = defaultdict(list)
    for node, next_node, weight in b8:
        b1[node].append((weight, next_node))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        cost, b5, b4 = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = end:
                return (cost, b4)
            for weight, next_node in b1.get(b5, ()):
                if next_node not in b3:
                    b6 = cost + weight
                    heappush(b2, (b6, next_node, b4))
    return float("inf")
if b7 = = "__main__":
    b8 = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "H", 5)
    ]
    print(fonk1(b8, "A", "H")))