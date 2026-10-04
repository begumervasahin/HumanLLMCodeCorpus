import networkx as nx
from kruskal import Algoritimo_kruskal as Kruskal
graph_data = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
    ]
}
mst_edges = [
    (1, 'A', 'B'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
]
def create_graph(vertices, edges):
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_weighted_edges_from(edges)
    return graph
main_graph = create_graph(graph_data['vertices'], graph_data['edges'])
mst_graph = create_graph(['A', 'B', 'C', 'D'], mst_edges)
test_graph_data = [
    (1, 2, 4),
    (1, 3, 8),
    (2, 3, 11),
    (2, 4, 8),
    (3, 6, 7),
    (3, 7, 1),
    (6, 4, 2),
    (6, 7, 20),
    (7, 8, 2),
    (4, 8, 4),
    (5, 8, 14),
    (5, 9, 9),
    (8, 9, 10),
    (4, 5, 7),
]
test_graph = create_graph([], test_graph_data)
kruskal = Kruskal()
mst_result = kruskal.kruskal(test_graph)
print("Edges of the minimum spanning tree:", mst_result.edges)
print("Total weight of the minimum spanning tree:", kruskal.peso(mst_result))