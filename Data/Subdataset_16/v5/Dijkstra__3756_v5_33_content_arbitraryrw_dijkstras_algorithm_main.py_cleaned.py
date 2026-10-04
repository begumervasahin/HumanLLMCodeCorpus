def fonk1(b5, b7):
    b1 = float("inf")
    b2 = None
    for b8, b9 in b5.items():
        if b9 < b1 and b8 not in b7:
            b1 = b9
            b2 = b8
    return b2
def fonk2():
    print("[+] Dijkstra's algorithm running!")
    b3 = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    b4 = float("inf")
    b5 = {
        "a": 6,
        "b": 2,
        "fin": b4
    }
    b6 = {
        "a": "start",
        "b": "start",
        "fin": None
    }
    b7 = []
    b8 = fonk1(b5, b7)
    while b8 is not None:
        b9 = b5[b8]
        b10 = b3[b8]
        for neighbor, weight in b10.items():
            b11 = b9 + weight
            if b5[neighbor] > b11:
                b5[neighbor] = b11
                b6[neighbor] = b8
        b7.append(b8)
        b8 = fonk1(b5, b7)
    print("Final b5 to each b8:", b5)
    print("Parents of each b8:", b6)
    print("Processed nodes in order:", b7)
if b12 = = "__main__":
    fonk2()