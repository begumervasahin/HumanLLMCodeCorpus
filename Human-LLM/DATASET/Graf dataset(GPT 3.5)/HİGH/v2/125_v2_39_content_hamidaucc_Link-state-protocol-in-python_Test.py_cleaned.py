from Graph import Graph
def fonk1():
    b1 = Graph.graphreader("graph1.txt")
    b2 = b1.get_node_by_label(1)
    b3 = b1.linkState(b2)
    for node, (length, predecessor) in sorted(b3.items()):
        print(f"Path from {b2} to Node {node}: Length: {length}. Preceding: {predecessor}")
        print("From Node: Cost")
        print(f"{node}       : {length} ({predecessor})")
def fonk2():
    b1 = Graph.graphreader("simplegraph2.txt")
    b2 = b1.get_node_by_label(14)
    b3 = b1.linkState(b2)
    for node, (length, predecessor) in sorted(b3.items()):
        print(f"Path from {b2} to Node {node}: Length: {length}. Preceding: {predecessor}")
        print("From Node: Cost")
        print(f"{node}       : {length} ({predecessor})")
if b4 = = "__main__":
    fonk1()
    fonk2()