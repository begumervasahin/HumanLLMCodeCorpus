
class Weighted_Graph:
    def __init__(self, filename):
        self.vertices = set()
        self.edges = {}
        with open(filename, 'r') as file:
            for line in file:
                v1, v2, weight = line.split()
                weight = int(weight)
                self.vertices.add(v1)
                self.vertices.add(v2)
                self.edges[(v1, v2)] = weight
                self.edges[(v2, v1)] = weight
    def edge_dict(self):
        return self.edges
    def edge_set(self):
        return set(self.edges.keys())
    def vertex_set(self):
        return self.vertices
from Weighted_Graph import Weighted_Graph
def c(edge, graph):
    return graph.edge_dict()[edge]
def incident_edges(T, graph):
    edges = set()
    for vertex in T[0]:
        for edge in graph.edge_set():
            if vertex in edge:
                edges.add(edge)
    return edges.difference(T[1])
def valid_edges(T, graph):
    edges = incident_edges(T, graph)
    not_valid = set()
    tree_vertices = set(T[0])
    non_tree_vertices = graph.vertex_set().difference(tree_vertices)
    for edge in edges:
        if edge[0] in tree_vertices and edge[1] in tree_vertices:
            not_valid.add(edge)
    return edges.difference(not_valid)
def min_valid_edge(T, graph):
    edges = valid_edges(T, graph)
    return min(edges, key=lambda edge: c(edge, graph))
def update(T, graph):
    vertices, edges = T
    new_edge = min_valid_edge(T, graph)
    new_edges = edges + [new_edge]
    new_vertices = set(vertices).union(new_edge)
    return (new_vertices, new_edges)
def total_sum(T, graph):
    return sum(c(edge, graph) for edge in T[1])
if __name__ == "__main__":
    graph = Weighted_Graph('test_graph.txt')
    start_vertex = 'A'
    T = ([start_vertex], [])
    while len(T[0]) < len(graph.vertex_set()):
        T = update(T, graph)
    print("Total cost of MST:", total_sum(T, graph))
    print("Edges in MST:", T[1])