from Weighted_Graph import Weighted_Graph
b1 = Weighted_Graph('test_graph.txt')
def fonk1(edge, graph):
    return graph.edge_dict()[edge]
def fonk2(tree, graph):
    vertices_in_tree, b2 = tree
    b3 = [
        edge for vertex in vertices_in_tree
        for edge in graph.edge_set()
        if vertex in edge and edge not in b2
    ]
    return b3
def fonk3(tree, graph):
    vertices_in_tree, b4 = tree
    b5 = graph.vertex_set()
    b6 = b5 - vertices_in_tree
    b7 = [
        edge for edge in fonk2(tree, graph)
        if not any(
            v in edge and u in edge
            for v in vertices_in_tree
            for u in b6
        )
    ]
    return b7
def fonk4(tree, graph):
    b8 = fonk3(tree, graph)
    b9 = min(b8, key=lambda e: fonk1(e, graph))
    return b9
def fonk5(tree, graph):
    vertices_in_tree, b2 = tree
    b10 = fonk4(tree, graph)
    b11 = b2 + [b10]
    b12 = vertices_in_tree | set(b10)
    return b12, b11
def fonk6(tree, graph):
    b4, b2 = tree
    return sum(fonk1(edge, graph) for edge in b2)