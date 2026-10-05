
from utils import initialize_single_source, extract_min, relax
def dijkstra(graph, source):
    initialize_single_source(graph, source)
    S = []
    Q = [v for v in graph.get_vertices()]
    while len(Q) > 0:
        u = extract_min(Q)
        u.set_visitado()
        S.append(u)
        for v in u.get_vertices_adjacentes():
            if v.get_visitado():
                continue
            relax(u, v)