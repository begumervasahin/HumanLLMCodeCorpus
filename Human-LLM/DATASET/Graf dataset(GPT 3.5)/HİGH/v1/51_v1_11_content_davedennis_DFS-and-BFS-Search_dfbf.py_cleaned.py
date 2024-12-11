import sys
def fonk1(filename, b1 = False):
    b2 = {}
    with open(filename, 'r') as file:
        for line in file:
            b3 = line.strip().split(" ")
            if b1:
                print("b3:", b3, "len(b3):", len(b3))
            if b3 = = ['']:
                continue
            b2[b3[0]] = ('white', b3[1:])
    return b2
def fonk2(b2):
    print("Dumping b2: nodeName (color, [adj list])")
    for node in b2:
        print(node, b2[node])
def fonk3(b2, b8):
    b4 = [(b8, 0)]
    b2[b8] = ("black", b2[b8][1], 0)
    b5 = []
    if len(b2[b8][1]) == 0:
        return b5
    while b4:
        node, b6 = b4.pop(0)
        for i in b2[node][1]:
            if b2[i][0] == "white":
                b2[i] = ('grey', b2[i][1], b6 + 1)
                b5.append((i, b2[i][2]))
                b4.append((i, b6 + 1))
        b2[node] = ("black", b2[node][1], b6)
    return b5
def fonk4(b2):
    for node in b2:
        b2[node] = ('white', b2[node][1])
def fonk5(b2, b8):
    b2[b8] = ("grey", b2[b8][1])
    for v in b2[b8][1]:
        if b2[v][0] == "white":
            fonk5(b2, v)
        if b2[v][0] == "grey":
            print("Cycle in {}".format(v))
    b2[b8] = ("black", b2[b8][1])
if b7 = = "__main__":
    b1 = len(sys.argv) > 4
    b2 = fonk1(sys.argv[1], b1)
    b8 = sys.argv[2]
    if b1:
        fonk2(b2)
    print("Root key:", b8)
    b2[b8] = ('black', b2[b8][1])
    b9 = fonk3(b2, b8)
    print("BFS")
    print(b9)
    if b1:
        fonk2(b2)
    fonk4(b2)
    if b1:
        fonk2(b2)
    print("DFS")
    fonk5(b2, b8)
    if b1:
        fonk2(b2)