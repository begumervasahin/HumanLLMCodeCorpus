import sys
def fonk1(filename, b1 = False):
    b2 = {}
    with open(filename, 'r') as file:
        for line in file:
            b3 = line.strip().split(" ")
            if not b3:
                continue
            b4 = b3[0]
            b5 = b3[1:]
            b2[b4] = {
                'color': 'white',
                'b5': b5
            }
            if b1:
                print("Node:", b4, "Adjacent b3:", b5)
    return b2
def fonk2(b2):
    print("Graph Contents: Node (Color, [Adjacent Nodes])")
    for node, data in b2.items():
        print(node, data)
def fonk3(b2, b11):
    b6 = [(b11, 0)]
    b2[b11]['color'] = "black"
    b7 = []
    if not b2[b11]['b5']:
        return b7
    while b6:
        node, b8 = b6.pop(0)
        for neighbor in b2[node]['b5']:
            if b2[neighbor]['color'] == "white":
                b2[neighbor]['color'] = 'grey'
                b7.append((neighbor, b8 + 1))
                b6.append((neighbor, b8 + 1))
        b2[node]['color'] = "black"
    return b7
def fonk4(b2, b11, b9 = None):
    b2[b11]['color'] = "grey"
    for neighbor in b2[b11]['b5']:
        if b2[neighbor]['color'] == "white":
            fonk4(b2, neighbor, b11)
        elif b2[neighbor]['color'] == "grey" and neighbor != b9:
            print("Cycle detected between b3:", b11, "and", neighbor)
    b2[b11]['color'] = "black"
if b10 = = "__main__":
    b1 = len(sys.argv) > 4
    b2 = fonk1(sys.argv[1], b1)
    b11 = sys.argv[2]
    print("Root key:", b11)
    b12 = fonk3(b2, b11)
    print("BFS Result:")
    print(b12)
    for node in b2:
        b2[node]['color'] = 'white'
    print("DFS Result:")
    fonk4(b2, b11)