def fonk1(input_file):
    b1 = open(input_file, 'r', encoding="utf8")
    b2 = []
    b3 = []
    b4 = []
    for k in range(int(b1.readline())):
        b3.append(b1.readline().split())
        b4.append({str(k + 1)})
        for l in range(int(b1.readline())):
            b5 = b1.readline().split()
            b2.append([str(k + 1), str(b5[0]), int(b5[1])])
    return b2, b3, b4
def fonk2(b2):
    for i in b2:
        for p in b2:
            if i[0] == p[1] and i[1] == p[0] and i[2] == p[2]:
                b2.remove(p)
    b2.sort(b6 = lambda x: x[2])
    return b2
def fonk3(b2, b4):
    a1 = 0
    b7 = []
    for e in b2:
        for s in b4:
            if {e[0]}.issubset(s):
                b8 = b4.index(s)
            if {e[1]}.issubset(s):
                b9 = b4.index(s)
        if b8 != b9 and len(b4) != 1:
            b7.append([e[0], e[1], e[2]])
            b4[b8] = b4[b8].union(b4[b9])
            b4.remove(b4[b9])
            a1 += e[2]
    return a1, b7
def fonk4(input_file):
    b11, names, b10 = fonk1(input_file)
    b11 = fonk2(b11)
    mst, b7 = fonk3(b11, b10)
    print("The Lenght of Minimum Spanning Tree:", mst)
fonk4('tr_districts_IDs.txt')