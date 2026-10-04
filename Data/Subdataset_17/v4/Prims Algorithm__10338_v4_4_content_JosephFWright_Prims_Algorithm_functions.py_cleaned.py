from Weighted_Graph import Weighted_Graph
G = Weighted_Graph('test_graph.txt')
def cost(e, G):
    return G.edge_dict()[e]
def incident_edges(T, G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e and e not in edges:
                edges.append(e)
    for e in edges.copy():
        if e in T[1]:
            edges.remove(e)
    return edges
def valid_edges(T, G):
    edges = incident_edges(T, G)
    not_valid = incident_edges(T, G)
    vlist = G.vertex_set().difference(set(T[0]))
    for v in T[0]:
        for x in vlist:
            for e in G.edge_set():
                if v in e and x in e and e in edges:
                    not_valid.remove(e)
    valid_edges = list(set(edges) - set(not_valid))
    return valid_edges
def min_valid_edge(T, G):
    edges = valid_edges(T, G)
    min_edge = edges[0]
    for e in edges:
        if cost(e, G) < cost(min_edge, G):
            min_edge = e
    return min_edge
def update_tree(T, G):
    vertices = set(T[0])
    edges = list(T[1])
    new_edge = min_valid_edge(T, G)
    edges.append(new_edge)
    for v in new_edge:
        if v in G.vertex_set() and v not in vertices:
            vertices.add(v)
    return [vertices, edges]
def total_cost(T, G):
    return sum(cost(e, G) for e in T[1])