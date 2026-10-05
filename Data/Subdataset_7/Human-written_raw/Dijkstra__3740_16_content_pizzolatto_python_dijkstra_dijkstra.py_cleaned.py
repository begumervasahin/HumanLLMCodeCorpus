b1 = {}
b1["inicio"] = {}
b1["inicio"]["a"] = 6
b1["inicio"]["b"] = 2
b1["a"] = {}
b1["a"]["fim"] = 1
b1["b"] = {}
b1["b"]["a"] = 3
b1["b"]["fim"] = 5
b1["fim"] = {}
b2 = float("inf")
b3 = {}
b3["a"] = 6
b3["b"] = 2
b3["fim"] = b2
b4 = {}
b4["a"] = "inicio"
b4["b"] = "inicio"
b4["fim"] = None
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