from DirectedGraphClass import DirectedGraph
def create_directed_graph(directed_graph, source):
    directed_graph.add_edge(0, 1, 6)
    directed_graph.add_edge(0, 3, 7)
    directed_graph.add_edge(1, 2, 5)
    directed_graph.add_edge(1, 3, 8)
    directed_graph.add_edge(1, 4, -4)
    directed_graph.add_edge(2, 1, -2)
    directed_graph.add_edge(3, 2, -3)
    directed_graph.add_edge(3, 4, 9)
    directed_graph.add_edge(4, 0, 2)
    directed_graph.add_edge(4, 2, 7)
def bellman_ford_function(directed_graph):
    V = directed_graph.num_vertices()
    source = 0
    dist = [float('inf')] * V
    pred = [-1] * V
    dist[source] = 0
    for _ in range(V - 1):
        for u, v, w in directed_graph.get_edges():
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
    for u, v, w in directed_graph.get_edges():
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative cycle")
            return
    directed_graph.set_shortest_path(dist, pred)
    return directed_graph
def main():
    number_of_vertices = 5
    source_vertex = 0
    directed_graph_var = DirectedGraph(number_of_vertices)
    create_directed_graph(directed_graph_var, source_vertex)
    directed_graph_var = bellman_ford_function(directed_graph_var)
    if directed_graph_var:
        directed_graph_var.print_shortest_path()
if __name__ == "__main__":
    main()