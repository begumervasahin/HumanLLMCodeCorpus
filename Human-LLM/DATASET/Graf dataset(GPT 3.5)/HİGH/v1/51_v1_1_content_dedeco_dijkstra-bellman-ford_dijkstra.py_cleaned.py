
from utils import initialize_single_source, extract_min, relax
def fonk1(graph, source):
    initialize_single_source(graph, source)
    b1 = []
    b2 = [v for v in graph.get_vertices()]
    while len(b2) > 0:
        b3 = extract_min(b2)
        b3.set_visitado()
        b1.append(b3)
        for v in b3.get_vertices_adjacentes():
            if v.get_visitado():
                continue
            relax(b3, v)