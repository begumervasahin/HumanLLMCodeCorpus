
def Kruskals(edge_file_name, start_vertex=0):
    G = Weighted_Graph(edge_file_name)
    F = ({G.vertex_set()}, [])
    while not is_connected(F):
        min_cost_edge = find_min_cost_edge(G, F)
        add_edge_to_forest(F, min_cost_edge)
    return F
def is_connected(F):
    pass
def find_min_cost_edge(G, F):
    pass
def add_edge_to_forest(F, edge):
    pass