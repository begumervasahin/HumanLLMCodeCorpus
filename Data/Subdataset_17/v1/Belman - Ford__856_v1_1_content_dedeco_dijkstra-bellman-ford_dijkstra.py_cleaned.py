from utils import initialize_single_source, extract_min, relax
def dijkstra(graph, source):
    initialize_single_source(graph, source)
    visited_nodes = []
    priority_queue = [v for v in graph.get_vertices()]
    while priority_queue:
        u = extract_min(priority_queue)
        u.set_visited()
        visited_nodes.append(u)
        for v in u.get_adjacent_vertices():
            if v.is_visited():
                continue
            relax(u, v)
if __name__ == "__main__":
    from utils import Graph, Vertex
    graph = Graph()
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
        (3, 4, 3)
    ]
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    source_vertex = graph.get_vertex(0)
    dijkstra(graph, source_vertex)
    for vertex in graph.get_vertices():
        print(f"Distance from {source_vertex.id} to {vertex.id} is {vertex.get_distance()}")