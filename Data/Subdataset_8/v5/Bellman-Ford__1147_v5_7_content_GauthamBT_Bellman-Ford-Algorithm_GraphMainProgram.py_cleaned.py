from DirectedGraphClass import DirectedGraph
def create_sample_graph(graph):
    graph.add_edge(0, 1, weight=6)
    graph.add_edge(0, 3, weight=7)
    graph.add_edge(1, 2, weight=5)
    graph.add_edge(1, 3, weight=8)
    graph.add_edge(1, 4, weight=-4)
    graph.add_edge(2, 1, weight=-2)
    graph.add_edge(3, 2, weight=-3)
    graph.add_edge(3, 4, weight=9)
    graph.add_edge(4, 0, weight=2)
    graph.add_edge(4, 2, weight=7)
def run_bellman_ford(graph):
    graph.bellman_ford()
def main():
    num_vertices = 5
    directed_graph = DirectedGraph(num_vertices)
    create_sample_graph(directed_graph)
    run_bellman_ford(directed_graph)
    source_vertex = 0
    directed_graph.print_shortest_paths(source_vertex)
if __name__ == "__main__":
    main()