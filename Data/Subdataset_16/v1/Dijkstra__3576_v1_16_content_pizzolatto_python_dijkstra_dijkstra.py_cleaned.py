
b1 = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}
b2 = float("inf")
b3 = {
    "a": 6,
    "b": 2,
    "fim": b2
}
b4 = {
    "a": "inicio",
    "b": "inicio",
    "fim": None
}
b5 = []
def fonk1(b3):
    b6 = float("inf")
    b7 = None
    for b9 in b3:
        b8 = b3[b9]
        if b8 < b6 and b9 not in b5:
            b6 = b8
            b7 = b9
    return b7
b9 = fonk1(b3)
while b9 is not None:
    b8 = b3[b9]
    b10 = b1[b9]
    for n in b10.keys():
        b11 = b8 + b10[n]
        if b3[n] > b11:
            b3[n] = b11
            b4[n] = b9
    b5.append(b9)
    b9 = fonk1(b3)
print(b3)