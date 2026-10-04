from Weighted_Graph import Weighted_Graph
G = Weighted_Graph('test_graph.txt')
def cost(edge, graph):
    return graph.edge_dict()[edge]
def incident_edges(tree, graph):
    vertices_in_tree, edges_in_tree = tree
    possible_edges = [
        edge for vertex in vertices_in_tree
        for edge in graph.edge_set()
        if vertex in edge and edge not in edges_in_tree
    ]
    return possible_edges
def valid_edges(tree, graph):
    vertices_in_tree, _ = tree
    all_vertices = graph.vertex_set()
    vertices_not_in_tree = all_vertices - vertices_in_tree
    valid_edges_list = [
        edge for edge in incident_edges(tree, graph)
        if not any(
            v in edge and u in edge
            for v in vertices_in_tree
            for u in vertices_not_in_tree
        )
    ]
    return valid_edges_list
def min_valid_edge(tree, graph):
    edges = valid_edges(tree, graph)
    min_edge = min(edges, key=lambda e: cost(e, graph))
    return min_edge
def update_tree(tree, graph):
    vertices_in_tree, edges_in_tree = tree
    new_edge = min_valid_edge(tree, graph)
    updated_edges = edges_in_tree + [new_edge]
    updated_vertices = vertices_in_tree | set(new_edge)
    return updated_vertices, updated_edges
def total_cost(tree, graph):
    _, edges_in_tree = tree
    return sum(cost(edge, graph) for edge in edges_in_tree)