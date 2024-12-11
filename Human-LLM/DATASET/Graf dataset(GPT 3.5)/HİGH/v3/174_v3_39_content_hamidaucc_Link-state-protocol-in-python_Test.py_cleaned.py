from Graph import Graph
def fonk1(b2, b3):
    for node, (length, predecessor) in sorted(b3.items()):
        print(f"Path from {b2} to Node {node}: Length: {length}. Preceding: {predecessor}")
        print("From Node: Cost")
        print(f"{node}       : {length} ({predecessor})")
def fonk2(graph_file, src_label):
    b1 = Graph.graphreader(graph_file)
    b2 = b1.get_node_by_label(src_label)
    b3 = b1.linkState(b2)
    fonk1(b2, b3)
def fonk3():
    fonk2("graph1.txt", 1)
def fonk4():
    fonk2("simplegraph2.txt", 14)
if b4 = = "__main__":
    fonk3()
    fonk4()