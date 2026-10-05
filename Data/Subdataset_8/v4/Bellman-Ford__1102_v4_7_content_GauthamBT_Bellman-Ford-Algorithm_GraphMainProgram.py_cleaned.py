from DirectedGraphClass import DirectedGraph
def create_directed_graph(graph, source_vertex):
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)
def run_bellman_ford_algorithm(graph):
    graph.bellman_ford()
def main():
    num_vertices = 5
    directed_graph = DirectedGraph(num_vertices)
    create_directed_graph(directed_graph, source_vertex=0)
    run_bellman_ford_algorithm(directed_graph)
    directed_graph.print_shortest_paths(source_vertex=0)
if __name__ == "__main__":
    main()