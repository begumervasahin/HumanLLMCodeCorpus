from utils import initialize_single_source, relax
def fonk1(b2, source):
    initialize_single_source(b2, source)
    for _ in range(len(b2.get_vertices()) - 1):
        for u, v in b2.get_edges():
            if not v.is_visited():
                relax(u, v)
    for u, v in b2.get_edges():
        if v.get_distance() > u.get_distance() + u.get_weight(v):
            return False
    return True
if b1 = = "__main__":
    from utils import Graph, Vertex
    b2 = Graph()
    b3 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in b3:
        b2.add_edge(u, v, w)
    b4 = b2.get_vertex(0)
    if fonk1(b2, b4):
        print("No negative weight cycle detected")
    else:
        print("Graph contains a negative weight cycle")