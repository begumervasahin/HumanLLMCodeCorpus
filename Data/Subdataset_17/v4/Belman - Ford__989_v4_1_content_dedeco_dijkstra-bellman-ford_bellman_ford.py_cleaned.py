from utils import initialize_single_source, relax
def bellman_ford(graph, source):
    initialize_single_source(graph, source)
    for _ in range(len(graph.get_vertices()) - 1):
        for u, v in graph.get_edges():
            if not v.is_visited():
                relax(u, v)
    for u, v in graph.get_edges():
        if v.get_distance() > u.get_distance() + u.get_weight(v):
            return False
    return True
if __name__ == "__main__":
    from utils import Graph, Vertex
    graph = Graph()
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    source_vertex = graph.get_vertex(0)
    if bellman_ford(graph, source_vertex):
        print("No negative weight cycle detected")
    else:
        print("Graph contains a negative weight cycle")