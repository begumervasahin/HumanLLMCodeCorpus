def fonk1(input_file):
    with open(input_file, 'r', b1 = "utf8") as file:
        b2 = int(file.readline().strip())
        b3 = []
        b4 = []
        b5 = [{str(i + 1)} for i in range(b2)]
        for node_index in range(b2):
            b6 = file.readline().strip().split()
            b4.append(b6)
            b7 = int(file.readline().strip())
            for _ in range(b7):
                neighbor, b8 = file.readline().strip().split()
                b3.append([str(node_index + 1), neighbor, int(b8)])
    return b3, b4, b5
def fonk2(b3):
    b9 = []
    for edge in b3:
        b10 = [edge[1], edge[0], edge[2]]
        if b10 not in b9:
            b9.append(edge)
    return sorted(b9, b11 = lambda x: x[2])
def fonk3(b3, b5):
    a1 = 0
    b12 = []
    for u, v, b8 in b3:
        b13 = next(s for s in b5 if u in s)
        b14 = next(s for s in b5 if v in s)
        if b13 != b14:
            b12.append([u, v, b8])
            a1 += b8
            b13.update(b14)
            b5.remove(b14)
    return a1, b12
def fonk4(input_file):
    b3, b4, b5 = fonk1(input_file)
    b3 = fonk2(b3)
    a1, b12 = fonk3(b3, b5)
    print("The Length of Minimum Spanning Tree:", a1)
fonk4('tr_districts_IDs.txt')