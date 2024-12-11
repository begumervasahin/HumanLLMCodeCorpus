
print("[+] Dijkstra's algorithm running!")
b1 = float("inf")
b2 = []
b3 = {
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}
b4 = {
    "a": 6,
    "b": 2,
    "fin": b1
}
b5 = {
    "a": "start",
    "b": "start",
    "fin": None
}
def fonk1(b4):
    a1 = b1
    b6 = None
    for node, b8 in b4.items():
        if b8 < a1 and node not in b2:
            a1 = b8
            b6 = node
    return b6
b7 = fonk1(b4)
while b7 is not None:
    b8 = b4[b7]
    b9 = b3[b7]
    for neighbor, edge_cost in b9.items():
        b10 = b8 + edge_cost
        if b4[neighbor] > b10:
            b4[neighbor] = b10
            b5[neighbor] = b7
    b2.append(b7)
    b7 = fonk1(b4)
print("Costs:", b4)
print("Parents:", b5)
print("Processed Nodes:", b2)