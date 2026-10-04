from collections import defaultdict
from heapq import heappop, heappush
def fonk1(b8, start, end):
    b1 = defaultdict(list)
    for src, dest, cost in b8:
        b1[src].append((cost, dest))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        cost, b5, b4 = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = end:
                return cost, b4
            for cost_to_neighbor, neighbor in b1[b5]:
                if neighbor not in b3:
                    heappush(b2, (cost + cost_to_neighbor, neighbor, b4))
    return float("inf"), ()
def fonk2(result):
    cost, b4 = result
    b6 = []
    while b4:
        node, b4 = b4
        b6.append(node)
    print(f"Cost: {cost}")
    print("Path:", " -> ".join(reversed(b6)))
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
    print("=== b9 = ==")
    b10 = [("A", "H"), ("A", "D"), ("D", "F"), ("F", "G"), ("G", "H"), ("F", "G")]
    for start_node, end_node in b10:
        print(f"{start_node} -> {end_node}:")
        fonk2(fonk1(b8, start_node, end_node))