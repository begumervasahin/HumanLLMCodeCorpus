from utils import initialize_single_source, relax
def bellman_ford(graph, source):
    initialize_single_source(graph, source)
    for _ in range(len(graph.get_vertices()) - 1):
        for u in graph.get_vertices():
            for u, v, weight in graph.get_edges():
                if v.is_visited():
                    continue
                relax(u, v)
    for u, v, weight in graph.get_edges():
        if v.get_distance() > u.get_distance() + weight:
            return False
    return True
