from Graph import Graph
def print_shortest_paths(src, shortest_paths):
    for node, (length, predecessor) in sorted(shortest_paths.items()):
        print(f"Path from {src} to Node {node}: Length: {length}. Preceding: {predecessor}")
        print("From Node: Cost")
        print(f"{node}       : {length} ({predecessor})")
def test_graph(graph_file, src_label):
    graph = Graph.graphreader(graph_file)
    src = graph.get_node_by_label(src_label)
    shortest_paths = graph.linkState(src)
    print_shortest_paths(src, shortest_paths)
def test1():
    test_graph("graph1.txt", 1)
def test2():
    test_graph("simplegraph2.txt", 14)
if __name__ == "__main__":
    test1()
    test2()