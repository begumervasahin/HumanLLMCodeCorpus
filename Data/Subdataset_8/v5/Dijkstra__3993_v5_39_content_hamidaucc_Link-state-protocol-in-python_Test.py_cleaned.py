from Graph import Graph
def print_shortest_paths(src, shortest_paths):
    for node, (length, predecessor) in sorted(shortest_paths.items()):
        print(f"Path from {src} to Node {node}: Length: {length}. Preceding: {predecessor}")
def test_graph(graph_file, src_label):
    graph = Graph.graphreader(graph_file)
    src_node = graph.get_node_by_label(src_label)
    shortest_paths = graph.linkState(src_node)
    print_shortest_paths(src_node, shortest_paths)
def test1():
    graph_file = "graph1.txt"
    src_label = 1
    test_graph(graph_file, src_label)
def test2():
    graph_file = "simplegraph2.txt"
    src_label = 14
    test_graph(graph_file, src_label)
if __name__ == "__main__":
    test1()
    test2()