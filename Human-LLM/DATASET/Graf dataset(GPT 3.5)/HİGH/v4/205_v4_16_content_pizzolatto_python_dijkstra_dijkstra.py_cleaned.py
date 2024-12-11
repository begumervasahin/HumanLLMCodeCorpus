
b1 = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}
b2 = float("inf")
b3 = {"a": 6, "b": 2, "fim": b2}
b4 = {"a": "inicio", "b": "inicio", "fim": None}
b5 = []
def fonk1(b3, b5):
    a1 = b2
    b6 = None
    for b8 in b3:
        b7 = b3[b8]
        if b7 < a1 and b8 not in b5:
            a1 = b7
            b6 = b8
    return b6
b8 = fonk1(b3, b5)
while b8 is not None:
    b7 = b3[b8]
    b9 = b1[b8]
    for neighbor in b9:
        b10 = b7 + b9[neighbor]
        if b3[neighbor] > b10:
            b3[neighbor] = b10
            b4[neighbor] = b8
    b5.append(b8)
    b8 = fonk1(b3, b5)
print(b3)