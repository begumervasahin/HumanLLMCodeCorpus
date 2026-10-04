import networkx as nx
from b8 import Algoritimo_kruskal as Kruskal
b1 = {
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
b2 = [
    (1, 'A', 'B'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
]
def fonk1(vertices, edges):
    b3 = nx.Graph()
    b3.add_nodes_from(vertices)
    b3.add_weighted_edges_from(edges)
    return b3
b4 = fonk1(b1['vertices'], b1['edges'])
b5 = fonk1(['A', 'B', 'C', 'D'], b2)
b6 = [
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
b7 = fonk1([], b6)
b8 = Kruskal()
b9 = b8.b8(b7)
print("Edges of the minimum spanning tree:", b9.edges)
print("Total weight of the minimum spanning tree:", b8.peso(b9))