def fonk1(input_file):
    with open(input_file, 'r', b1 = "utf8") as file:
        b2 = int(file.readline().strip())
        b3 = []
        b4 = []
        b5 = [{str(i + 1)} for i in range(b2)]
        for i in range(b2):
            b4.append(file.readline().split())
            b6 = int(file.readline().strip())
            for _ in range(b6):
                node, b7 = file.readline().split()
                b3.append([str(i + 1), node, int(b7)])
    return b3, b4, b5
def fonk2(b3):
    b8 = []
    for edge in b3:
        if not any(e[0] == edge[1] and e[1] == edge[0] and e[2] == edge[2] for e in b8):
            b8.append(edge)
    b8.sort(b9 = lambda x: x[2])
    return b8
def fonk3(b3, b5):
    a1 = 0
    b10 = []
    for edge in b3:
        u, v, b7 = edge
        b11 = next(s for s in b5 if u in s)
        b12 = next(s for s in b5 if v in s)
        if b11 != b12:
            b10.append(edge)
            a1 += b7
            b11.update(b12)
            b5.remove(b12)
        if len(b5) == 1:
            break
    return a1, b10
def fonk4(input_file):
    b3, b4, b5 = fonk1(input_file)
    b3 = fonk2(b3)
    a1, b10 = fonk3(b3, b5)
    print("The Length of Minimum Spanning Tree:", a1)
    for edge in b10:
        print(f"Edge: {edge[0]} -> {edge[1]} with b7 {edge[2]}")
fonk4('tr_districts_IDs.txt')