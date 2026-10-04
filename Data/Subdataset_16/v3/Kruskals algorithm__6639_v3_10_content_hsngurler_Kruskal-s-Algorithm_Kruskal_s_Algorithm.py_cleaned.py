def fonk1(input_file):
    with open(input_file, 'r', b1 = "utf8") as file:
        b2 = int(file.readline().strip())
        b3 = []
        b4 = [{str(i + 1)} for i in range(b2)]
        b5 = [file.readline().split() for _ in range(b2)]
        for i in range(b2):
            b6 = int(file.readline().strip())
            for _ in range(b6):
                node, b7 = file.readline().split()
                b3.append([str(i + 1), node, int(b7)])
    return b3, b5, b4
def fonk2(b3):
    b8 = []
    for edge in b3:
        if not any(e[0] == edge[1] and e[1] == edge[0] and e[2] == edge[2] for e in b8):
            b8.append(edge)
    return sorted(b8, b9 = lambda x: x[2])
def fonk3(b3, b4):
    a1 = 0
    b10 = []
    for u, v, b7 in b3:
        b11 = next(s for s in b4 if u in s)
        b12 = next(s for s in b4 if v in s)
        if b11 != b12:
            b10.append([u, v, b7])
            a1 += b7
            b11.update(b12)
            b4.remove(b12)
        if len(b4) == 1:
            break
    return a1, b10
def fonk4(input_file):
    b3, b5, b4 = fonk1(input_file)
    b13 = fonk2(b3)
    a1, b10 = fonk3(b13, b4)
    print(f"The Length of Minimum Spanning Tree: {a1}")
    for u, v, b7 in b10:
        print(f"Edge: {u} -> {v} with b7 {b7}")
fonk4('tr_districts_IDs.txt')