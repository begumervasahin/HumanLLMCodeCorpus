from collections import defaultdict
b1 = defaultdict(dict)
b1["inicio"]["a"] = 6
b1["inicio"]["b"] = 2
b1["a"]["fim"] = 1
b1["b"]["a"] = 3
b1["b"]["fim"] = 5
b2 = float("inf")
b3 = {"a": 6, "b": 2, "fim": b2}
b4 = {"a": "inicio", "b": "inicio", "fim": None}
b5 = []
def fonk1(b3, b5):
    a1 = b2
    b6 = None
    for b7, b8 in b3.items():
        if b8 < a1 and b7 not in b5:
            a1 = b8
            b6 = b7
    return b6
b7 = fonk1(b3, b5)
while b7 is not None:
    b8 = b3[b7]
    b9 = b1[b7]
    for neighbor, neighbor_cost in b9.items():
        b10 = b8 + neighbor_cost
        if b3[neighbor] > b10:
            b3[neighbor] = b10
            b4[neighbor] = b7
    b5.append(b7)
    b7 = fonk1(b3, b5)
print(b3)