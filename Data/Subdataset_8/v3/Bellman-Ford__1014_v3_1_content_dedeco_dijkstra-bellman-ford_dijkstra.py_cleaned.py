from utils import initialize_single_source, extract_min, relax
def dijkstra(graph, source):
    initialize_single_source(graph, source)
    visited_vertices = []
    unvisited_vertices = list(graph.get_vertices())
    while unvisited_vertices:
        current_vertex = extract_min(unvisited_vertices)
        current_vertex.set_visited()
        visited_vertices.append(current_vertex)
        for adjacent_vertex in current_vertex.get_adjacent_vertices():
            if adjacent_vertex.is_visited():
                continue
            relax(current_vertex, adjacent_vertex)