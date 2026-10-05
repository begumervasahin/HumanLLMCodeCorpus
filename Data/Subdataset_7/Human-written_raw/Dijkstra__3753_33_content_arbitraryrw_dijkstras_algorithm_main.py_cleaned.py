print("[+] Dijkstra's algorithm running!")
b1 = float("inf")
b2 = []
b3 = dict()
b3["a"] = dict()
b3["a"]["fin"] = 1
b3["b"] = dict()
b3["b"]["a"] = 3
b3["b"]["fin"] = 5
b3["fin"] = dict()
b4 = dict()
b4["a"] = 6
b4["b"] = 2
b4["fin"] = b1
b5 = dict()
b5["a"] = "start"
b5["b"] = "start"
b5["fin"] = None
def fonk1(b4):
    a1 = b1
    b6 = None
    for b8 in b4:
        b7 = b4[b8]
        if b7 < a1 and b8 not in b2:
            a1 = b7
            b6 = b8
    return b6
b8 = fonk1(b4)
while b8 is not None:
    b7 = b4[b8]
    b9 = b3[b8]
    for n in b9.keys():
        b10 = b7 + b9[n]
        if b4[n] > b10:
            b4[n] = b10
            b5[n] = b8
    b2.append(b8)
    b8 = fonk1(b4)
print(b4)
print(b5)
print(b2)