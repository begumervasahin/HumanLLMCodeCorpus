import sys
def fonk1(graph, source):
    for vertex in graph.get_vertices():
        vertex.set_distance(sys.maxsize)
    graph.get_vertex(source).set_distance(0)
def fonk2(queue):
    b1 = queue[0]
    for vertex in queue:
        if vertex.get_distance() < b1.get_distance():
            b1 = vertex
    queue.remove(b1)
    return b1
def fonk3(start_vertex, end_vertex):
    b2 = start_vertex.get_distance() + start_vertex.get_weight(end_vertex)
    if end_vertex.get_distance() > b2:
        end_vertex.set_distance(b2)
        end_vertex.set_previous(start_vertex)
def fonk4(vertex, path):
    if vertex.get_previous():
        path.append(vertex.get_previous().get_id())
        fonk4(vertex.get_previous(), path)
    return path