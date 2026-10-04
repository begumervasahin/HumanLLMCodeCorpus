from Graph import Graph
def fonk1(b2, b3):
    for node, (path_length, preceding_node) in sorted(b3.items()):
        print(f"Path from {b2} to Node {node}: Length: {path_length}. Preceding: {preceding_node}")
    print("\nFrom Node: Cost")
    for node, (path_length, preceding_node) in sorted(b3.items()):
        print(f"{node}       : {path_length} ({preceding_node})")
def fonk2(graph_file, src_label):
    b1 = Graph.graphreader(graph_file)
    b2 = b1.get_node_by_label(src_label)
    b3 = b1.linkState(b2)
    fonk1(b2, b3)
if b4 = = "__main__":
    print("Test 1:")
    fonk2("graph1.txt", 1)
    print("\nTest 2:")
    fonk2("simplegraph2.txt", 14)