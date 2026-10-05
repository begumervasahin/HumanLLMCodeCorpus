import sys
def initialize_single_source(graph, source):
    for vertex in graph.get_vertices():
        vertex.set_distance(sys.maxsize)
    graph.get_vertex(source).set_distance(0)
def extract_min(queue):
    min_vertex = queue[0]
    for vertex in queue:
        if vertex.get_distance() < min_vertex.get_distance():
            min_vertex = vertex
    queue.remove(min_vertex)
    return min_vertex
def relax(start_vertex, end_vertex):
    new_distance = start_vertex.get_distance() + start_vertex.get_weight(end_vertex)
    if end_vertex.get_distance() > new_distance:
        end_vertex.set_distance(new_distance)
        end_vertex.set_previous(start_vertex)
def shortest_path_to_vertex(vertex, path):
    if vertex.get_previous():
        path.append(vertex.get_previous().get_id())
        shortest_path_to_vertex(vertex.get_previous(), path)
    return path