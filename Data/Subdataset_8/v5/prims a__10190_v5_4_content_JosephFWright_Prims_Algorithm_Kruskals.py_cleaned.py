
def kruskals_minimum_spanning_tree(edge_file_name, start_vertex=0):
    graph = Weighted_Graph(edge_file_name)
    forest = ({graph.vertex_set()}, [])
    while not is_connected(forest):
        min_cost_edge = find_min_cost_edge(graph, forest)
        add_edge_to_forest(forest, min_cost_edge)
    return forest
def is_connected(forest):
    pass
def find_min_cost_edge(graph, forest):
    pass
def add_edge_to_forest(forest, edge):
    pass