from utils import initialize_single_source, relax
def bellman_ford(graph, source):
    initialize_single_source(graph, source)
    num_vertices = len(graph.get_vertices())
    for _ in range(num_vertices - 1):
        for u in graph.get_vertices():
            for edge_source, edge_dest, weight in graph.get_edges():
                if edge_dest.is_visited():
                    continue
                relax(edge_source, edge_dest)
    for edge_source, edge_dest, weight in graph.get_edges():
        if edge_dest.get_distance() > edge_source.get_distance() + weight:
            return False
    return True
