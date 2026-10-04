from collections import defaultdict
from heapq import heappop, heappush
def fonk1(b8, start, end):
    b1 = defaultdict(list)
    for node, next_node, weight in b8:
        b1[node].append((weight, next_node))
    b2 = [(0, start, ())]
    b3 = set()
    while b2:
        current_cost, b5, b4 = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = end:
                return current_cost, b4
            for weight, neighbor in b1[b5]:
                if neighbor not in b3:
                    heappush(b2, (current_cost + weight, neighbor, b4))
    return float("inf"), ()
def fonk2(b9):
    cost, b4 = b9
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
    b9 = fonk1(b8, "A", "H")
    print("Shortest b4 from A to H:")
    fonk2(b9)