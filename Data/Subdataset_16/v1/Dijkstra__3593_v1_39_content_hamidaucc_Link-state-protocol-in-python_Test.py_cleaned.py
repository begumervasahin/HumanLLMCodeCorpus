from Graph import Graph
def fonk1(b2, b3, b4):
    for element in sorted(b4):
        path_length, b1 = b4[element]
        print(f"Path from {b3} to Node {element}: Length: {path_length}. Preceding: {b1}")
    print("From Node: Cost")
    for element in sorted(b4):
        path_length, b1 = b4[element]
        print(f"{element}       : {path_length} ({b1})")
def fonk2():
    b2 = Graph.graphreader("graph1.txt")
    b3 = b2.get_node_by_label(1)
    b4 = b2.linkState(b3)
    fonk1(b2, b3, b4)
def fonk3():
    b2 = Graph.graphreader("simplegraph2.txt")
    b3 = b2.get_node_by_label(14)
    b4 = b2.linkState(b3)
    fonk1(b2, b3, b4)
if b5 = = "__main__":
    fonk2()
    fonk3()