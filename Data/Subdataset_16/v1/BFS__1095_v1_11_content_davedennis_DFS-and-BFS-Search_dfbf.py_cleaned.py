import sys
def fonk1(fnm, b8):
    b1 = open(fnm)
    b2 = {}
    for line in b1:
        b3 = line.strip().split(" ")
        if b8:
            print("b3:", b3, "len(b3):", len(b3))
        if b3 = = ['']: continue
        b2[b3[0]] = ('white', b3[1:])
    return b2
def fonk2(b2):
    print("Dumping b2: nodeName (color, [adj list])")
    for b6 in b2:
        print(b6, b2[b6])
def fonk3(b2, start_node):
    b4 = []
    b4.append(start_node)
    b2[start_node] = ("black", b2[start_node][1], 0)
    b5 = [(start_node, 0)]
    while b4:
        b6 = b4.pop(0)
        for i in b2[b6][1]:
            if b2[i][0] == "white":
                b2[i] = ('grey', b2[i][1], b2[b6][2] + 1)
                b5.append((i, b2[i][2]))
                b4.append(i)
        b2[b6] = ("black", b2[b6][1])
    return b5
def fonk4(b2):
    for b6 in b2:
        b2[b6] = ('white', b2[b6][1])
def fonk5(b2, b6):
    b2[b6] = ("grey", b2[b6][1])
    for v in b2[b6][1]:
        if b2[v][0] == "white":
            fonk5(b2, v)
        if b2[v][0] == "grey":
            print("Cycle in {}".format(v))
    b2[b6] = ("black", b2[b6][1])
if b7 = = "__main__":
    b8 = len(sys.argv) > 3
    b2 = fonk1(sys.argv[1], b8)
    b9 = sys.argv[2]
    if b8:
        fonk2(b2)
    print("Root key:", b9)
    b2[b9] = ('black', b2[b9][1])
    b10 = fonk3(b2, b9)
    print("BFS")
    print(b10)
    if b8:
        fonk2(b2)
    fonk4(b2)
    if b8:
        fonk2(b2)
    print("DFS")
    fonk5(b2, b9)
    if b8:
        fonk2(b2)