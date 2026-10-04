
b1 = {
    "start": {"a": 6, "b": 2},
    "a": {"end": 1},
    "b": {"a": 3, "end": 5},
    "end": {}
}
b2 = float("inf")
b3 = {
    "a": 6,
    "b": 2,
    "end": b2
}
b4 = {
    "a": "start",
    "b": "start",
    "end": None
}
b5 = []
def fonk1(b3):
    a1 = b2
    b6 = None
    for b7, b8 in b3.items():
        if b8 < a1 and b7 not in b5:
            a1 = b8
            b6 = b7
    return b6
b7 = fonk1(b3)
while b7 is not None:
    b8 = b3[b7]
    b9 = b1[b7]
    for neighbor in b9.keys():
        b10 = b8 + b9[neighbor]
        if b3[neighbor] > b10:
            b3[neighbor] = b10
            b4[neighbor] = b7
    b5.append(b7)
    b7 = fonk1(b3)
print("Costs to reach each b7:", b3)