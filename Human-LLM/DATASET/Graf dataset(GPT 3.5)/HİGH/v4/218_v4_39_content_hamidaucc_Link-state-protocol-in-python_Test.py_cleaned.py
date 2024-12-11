from Graph import Graph
def fonk1(b2, b3):
    for node, (length, predecessor) in sorted(b3.items()):
        print(f"Path from {b2} to Node {node}: Length: {length}. Preceding: {predecessor}")
def fonk2(b4, a1):
    b1 = Graph.graphreader(b4)
    b2 = b1.get_node_by_label(a1)
    b3 = b1.linkState(b2)
    fonk1(b2, b3)
def fonk3():
    b4 = "graph1.txt"
    a1 = 1
    fonk2(b4, a1)
def fonk4():
    b4 = "simplegraph2.txt"
    a1 = 14
    fonk2(b4, a1)
if b5 = = "__main__":
    fonk3()
    fonk4()