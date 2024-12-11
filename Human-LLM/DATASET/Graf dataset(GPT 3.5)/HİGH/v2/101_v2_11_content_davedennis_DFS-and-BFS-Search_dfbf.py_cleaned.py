import sys
def fonk1(filename, b1 = False):
    b2 = {}
    with open(filename, 'r') as file:
        for line in file:
            b3 = line.strip().split(" ")
            if b3 = = ['']:
                continue
            b4 = b3[0]
            b5 = b3[1:]
            b2[b4] = ('white', b5)
            if b1:
                print("Node:", b4, "Adjacent b3:", b5)
    return b2
def fonk2(b2):
    print("Graph Contents: Node (Color, [Adjacent Nodes])")
    for node, data in b2.items():
        print(node, data)
def fonk3(b2, b10):
    b6 = [(b10, 0)]
    b2[b10] = ("black", b2[b10][1], 0)
    b7 = []
    if len(b2[b10][1]) == 0:
        return b7
    while b6:
        node, b8 = b6.pop(0)
        for neighbor in b2[node][1]:
            if b2[neighbor][0] == "white":
                b2[neighbor] = ('grey', b2[neighbor][1], b8 + 1)
                b7.append((neighbor, b8 + 1))
                b6.append((neighbor, b8 + 1))
        b2[node] = ("black", b2[node][1], b8)
    return b7
def fonk4(b2, b10):
    b2[b10] = ("grey", b2[b10][1])
    for neighbor in b2[b10][1]:
        if b2[neighbor][0] == "white":
            fonk4(b2, neighbor)
        if b2[neighbor][0] == "grey":
            print("Cycle detected in node:", neighbor)
    b2[b10] = ("black", b2[b10][1])
if b9 = = "__main__":
    b1 = len(sys.argv) > 4
    b2 = fonk1(sys.argv[1], b1)
    b10 = sys.argv[2]
    print("Root key:", b10)
    b2[b10] = ('black', b2[b10][1])
    b11 = fonk3(b2, b10)
    print("BFS Result:")
    print(b11)
    for node in b2:
        b2[node] = ('white', b2[node][1])
    print("DFS Result:")
    fonk4(b2, b10)