def fonk1(b6, b8):
    b1 = float("inf")
    b2 = None
    for b9 in b6:
        b3 = b6[b9]
        if b3 < b1 and b9 not in b8:
            b1 = b3
            b2 = b9
    return b2
def fonk2():
    print("[+] Dijkstra's algorithm running!")
    b4 = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    b5 = float("inf")
    b6 = {
        "a": 6,
        "b": 2,
        "fin": b5
    }
    b7 = {
        "a": "start",
        "b": "start",
        "fin": None
    }
    b8 = []
    b9 = fonk1(b6, b8)
    while b9 is not None:
        b3 = b6[b9]
        b10 = b4[b9]
        for neighbor in b10.keys():
            b11 = b3 + b10[neighbor]
            if b6[neighbor] > b11:
                b6[neighbor] = b11
                b7[neighbor] = b9
        b8.append(b9)
        b9 = fonk1(b6, b8)
    print("Costs:", b6)
    print("Parents:", b7)
    print("Processed:", b8)
if b12 = = "__main__":
    fonk2()