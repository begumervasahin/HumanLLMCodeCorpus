from Graph import Graph
def fonk1(b2, b3, b4):
    for node in sorted(b4):
        path_length, b1 = b4[node]
        print(f"Path from {b3} to Node {node}: Length: {path_length}. Preceding: {b1}")
    print("\nFrom Node: Cost")
    for node in sorted(b4):
        path_length, b1 = b4[node]
        print(f"{node}       : {path_length} ({b1})")
def fonk2(graph_file, src_label):
    b2 = Graph.graphreader(graph_file)
    b3 = b2.get_node_by_label(src_label)
    b4 = b2.linkState(b3)
    fonk1(b2, b3, b4)
if b5 = = "__main__":
    print("Test 1:")
    fonk2("graph1.txt", 1)
    print("\nTest 2:")
    fonk2("simplegraph2.txt", 14)