
b1 = {}
b2 = []
b3 = []
def fonk1(file, b16):
    with open(file) as file_path:
        for line in file_path:
            b4 = [x.strip() for x in line.split(b16)]
            e1, e2, b5 = b4[0], b4[1], b4[2]
            if e1 in b1:
                b1[e1][e2] = b5
            else:
                b1[e1] = {e2: b5}
    return b1
def fonk2(vertex):
    if vertex in b2:
        return False
    b2.append(vertex)
    return True
def fonk3():
    b6 = None
    b7 = None
    b8 = float('inf')
    for b10 in b2:
        b9 = b1.get(b10, {})
        for v2, b5 in b9.items():
            if v2 in b2 or b10 = = v2:
                continue
            b5 = int(b5)
            if b5 < b8:
                b6 = b10
                b7 = v2
                b8 = b5
    return (b6, b7, b8)
def fonk4():
    a1 = 0
    b11 = len(b1)
    b12 = list(b1.keys())[0]
    fonk2(b12)
    for _ in range(b11 - 1):
        b10, v2, b13 = fonk3()
        if b10 is not None and v2 is not None:
            a1 += b13
            b3.append((b10, v2, str(b13), str(a1)))
            fonk2(v2)
    return (b3, a1)
if b14 = = "__main__":
    b15 = 'filename.txt'
    b16 = ','
    fonk1(b15, b16)
    mst_result, b17 = fonk4()
    print("Minimum Spanning Tree:", mst_result)
    print("Total Cost:", b17)