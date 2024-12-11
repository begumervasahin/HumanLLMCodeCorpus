import sys
def fonk1(file_name, b1 = False):
    b2 = {}
    with open(file_name) as file:
        for line in file:
            b3 = line.strip().split(" ")
            if not b3:
                continue
            node_name, b4 = b3[0], b3[1:]
            b2[node_name] = ('white', b4)
            if b1:
                print("Node:", node_name, "Adjacent Nodes:", b4)
    return b2
def fonk2(b2):
    print("Graph Structure: nodeName (color, [adjacent nodes])")
    for b7, data in b2.items():
        print(b7, data)
def fonk3(b2, root):
    b5 = []
    b5.append(root)
    b2[root] = ("black", b2[root][1], 0)
    if not b2[root][1]:
        return []
    b6 = [(root, 0)]
    while b5:
        b7 = b5.pop(0)
        for adj_node in b2[b7][1]:
            if b2[adj_node][0] == "white":
                b2[adj_node] = ('grey', b2[adj_node][1], b2[b7][2] + 1)
                b6.append((adj_node, b2[adj_node][2]))
                b5.append(adj_node)
        b2[b7] = ("black", b2[b7][1])
    return b6
def fonk4(b2, root):
    b8 = set()
    def fonk5(b7):
        b8.add(b7)
        b2[b7] = ("grey", b2[b7][1])
        for adj_node in b2[b7][1]:
            if adj_node not in b8:
                fonk5(adj_node)
            elif b2[adj_node][0] == "grey":
                print("Cycle detected in {}".format(adj_node))
        b2[b7] = ("black", b2[b7][1])
    fonk5(root)
if b9 = = "__main__":
    b1 = len(sys.argv) > 3
    b10 = sys.argv[1]
    b11 = sys.argv[2]
    b2 = fonk1(b10, b1)
    if b1:
        fonk2(b2)
    print("Root b7:", b11)
    b2[b11] = ('black', b2[b11][1])
    b12 = fonk3(b2, b11)
    print("BFS Result:")
    print(b12)
    if b1:
        fonk2(b2)
    for b7 in b2:
        b2[b7] = ('white', b2[b7][1])
    print("DFS:")
    fonk4(b2, b11)
    if b1:
        fonk2(b2)