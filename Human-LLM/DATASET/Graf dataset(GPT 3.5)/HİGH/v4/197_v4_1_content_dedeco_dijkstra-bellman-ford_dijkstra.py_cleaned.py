from utils import initialize_single_source, extract_min, relax
def fonk1(graph, source):
    initialize_single_source(graph, source)
    b1 = []
    b2 = [vertex for vertex in graph.get_vertices()]
    while len(b2) > 0:
        b3 = extract_min(b2)
        b3.set_visited()
        b1.append(b3)
        for adjacent_vertex in b3.get_adjacent_vertices():
            if adjacent_vertex.is_visited():
                continue
            relax(b3, adjacent_vertex)