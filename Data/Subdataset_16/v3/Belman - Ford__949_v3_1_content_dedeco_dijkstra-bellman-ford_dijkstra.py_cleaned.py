from utils import initialize_single_source, extract_min, relax
def fonk1(b5, source):
    initialize_single_source(b5, source)
    b1 = []
    b2 = list(b5.get_vertices())
    while b2:
        b3 = extract_min(b2)
        b3.set_visited()
        b1.append(b3)
        for v in b3.get_adjacent_vertices():
            if not v.is_visited():
                relax(b3, v)
if b4 = = "__main__":
    from utils import Graph, Vertex
    def fonk2():
        b5 = Graph()
        b6 = [
            (0, 1, 4),
            (0, 2, 1),
            (2, 1, 2),
            (1, 3, 1),
            (2, 3, 5),
            (3, 4, 3)
        ]
        for b3, v, w in b6:
            b5.add_edge(b3, v, w)
        return b5
    def fonk3(b5, b7):
        for vertex in b5.get_vertices():
            print(f"Distance from {b7.id} to {vertex.id} is {vertex.get_distance()}")
    b5 = fonk2()
    b7 = b5.get_vertex(0)
    fonk1(b5, b7)
    fonk3(b5, b7)