import sys
def fonk1(filename, b1 = False):
    b2 = {}
    with open(filename) as file:
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
    for node, details in b2.items():
        print(node, details)
def fonk3(b2, start_node):
    b4 = [start_node]
    b2[start_node] = ("black", b2[start_node][1], 0)
    b5 = [(start_node, 0)]
    while b4:
        b6 = b4.pop(0)
        for neighbor in b2[b6][1]:
            if b2[neighbor][0] == "white":
                b2[neighbor] = ('grey', b2[neighbor][1], b2[b6][2] + 1)
                b5.append((neighbor, b2[neighbor][2]))
                b4.append(neighbor)
        b2[b6] = ("black", b2[b6][1])
    return b5
def fonk4(b2):
    for node in b2:
        b2[node] = ('white', b2[node][1])
def fonk5(b2, node):
    b2[node] = ("grey", b2[node][1])
    for neighbor in b2[node][1]:
        if b2[neighbor][0] == "white":
            fonk5(b2, neighbor)
        elif b2[neighbor][0] == "grey":
            print(f"Cycle detected at node {neighbor}")
    b2[node] = ("black", b2[node][1])
if b7 = = "__main__":
    b1 = len(sys.argv) > 3
    b2 = fonk1(sys.argv[1], b1)
    b8 = sys.argv[2]
    if b1:
        fonk2(b2)
    print("Root key:", b8)
    b2[b8] = ('black', b2[b8][1])
    b9 = fonk3(b2, b8)
    print("BFS result:")
    print(b9)
    if b1:
        fonk2(b2)
    fonk4(b2)
    if b1:
        fonk2(b2)
    print("DFS result:")
    fonk5(b2, b8)
    if b1:
        fonk2(b2)