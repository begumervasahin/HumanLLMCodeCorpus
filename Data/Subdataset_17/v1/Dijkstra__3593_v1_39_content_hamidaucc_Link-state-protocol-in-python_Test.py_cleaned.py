from Graph import Graph
def display_link_state_results(graph, src, results):
    for element in sorted(results):
        path_length, preceding_node = results[element]
        print(f"Path from {src} to Node {element}: Length: {path_length}. Preceding: {preceding_node}")
    print("From Node: Cost")
    for element in sorted(results):
        path_length, preceding_node = results[element]
        print(f"{element}       : {path_length} ({preceding_node})")
def test1():
    graph = Graph.graphreader("graph1.txt")
    src = graph.get_node_by_label(1)
    results = graph.linkState(src)
    display_link_state_results(graph, src, results)
def test2():
    graph = Graph.graphreader("simplegraph2.txt")
    src = graph.get_node_by_label(14)
    results = graph.linkState(src)
    display_link_state_results(graph, src, results)
if __name__ == "__main__":
    test1()
    test2()