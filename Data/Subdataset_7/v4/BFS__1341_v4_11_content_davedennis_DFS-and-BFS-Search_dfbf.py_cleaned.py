import sys
def fonk1(file_name, b1 = False):
    b2 = {}
    with open(file_name) as file:
        for line in file:
            b3 = line.strip().split(" ")
            if b1:
                print("b3:", b3, "length:", len(b3))
            if b3 = = ['']:
                continue
            b2[b3[0]] = ('white', b3[1:])
    return b2
def fonk2(b2):
    print("Dumping b2: nodeName (color, [adjacent list]) ")
    for b6, data in b2.items():
        print(b6, data)
def fonk3(b2, b9):
    b4 = []
    b4.append(b9)
    b2[b9] = ("black", b2[b9][1], 0)
    if len(b2[b9][1]) == 0:
        return []
    b5 = [(b9, 0)]
    while b4:
        b6 = b4.pop(0)
        for adj_node in b2[b6][1]:
            if b2[adj_node][0] == "white":
                b2[adj_node] = ('grey', b2[adj_node][1], b2[b6][2] + 1)
                b5.append((adj_node, b2[adj_node][2]))
                b4.append(adj_node)
        b2[b6] = ("black", b2[b6][1])
    return b5
def fonk4(b2):
    for b6 in b2:
        b2[b6] = ('white', b2[b6][1])
def fonk5(b9):
    b7 = set()
    def fonk6(b6):
        b7.add(b6)
        b2[b6] = ("grey", b2[b6][1])
        for adj_node in b2[b6][1]:
            if adj_node not in b7:
                fonk6(adj_node)
            elif b2[adj_node][0] == "grey":
                print("Cycle in {}".format(adj_node))
        b2[b6] = ("black", b2[b6][1])
    fonk6(b9)
if b8 = = "__main__":
    b1 = len(sys.argv) > 3
    b2 = fonk1(sys.argv[1], b1)
    b9 = sys.argv[2]
    if b1:
        fonk2(b2)
    print("Root key:", b9)
    b2[b9] = ('black', b2[b9][1])
    b10 = fonk3(b2, b9)
    print("BFS:")
    print(b10)
    if b1:
        fonk2(b2)
    fonk4(b2)
    if b1:
        fonk2(b2)
    print("DFS:")
    fonk5(b9)
    if b1:
        fonk2(b2)