from Graph import Graph
def display_link_state_results(graph, src, results):
    for node in sorted(results):
        path_length, preceding_node = results[node]
        print(f"Path from {src} to Node {node}: Length: {path_length}. Preceding: {preceding_node}")
    print("\nFrom Node: Cost")
    for node in sorted(results):
        path_length, preceding_node = results[node]
        print(f"{node}       : {path_length} ({preceding_node})")
def run_test(graph_file, src_label):
    graph = Graph.graphreader(graph_file)
    src = graph.get_node_by_label(src_label)
    results = graph.linkState(src)
    display_link_state_results(graph, src, results)
if __name__ == "__main__":
    print("Test 1:")
    run_test("graph1.txt", 1)
    print("\nTest 2:")
    run_test("simplegraph2.txt", 14)