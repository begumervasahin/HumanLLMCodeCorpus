from kruskal import Algoritimo_kruskal as kr
import networkx as nx
b1 = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
b2 = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
b3 = nx.Graph()
b3.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
b3.add_edges_from([
                            ('A', 'B', {'weight': 1}),
                            ('A', 'C', {'weight': 5}),
                            ('A', 'D', {'weight': 3}),
                            ('B', 'C', {'weight': 4}),
                            ('B', 'D', {'weight': 2}),
                            ('C', 'D', {'weight': 1}),
                            ])
b4 = nx.Graph()
b4.add_nodes_from((['A', 'B', 'C', 'D']))
b4.add_edges_from([
                            ('A', 'B', {'weight': 1}),
                            ('B', 'D', {'weight': 2}),
                            ('C', 'D', {'weight': 1}),
                            ])
b5 = nx.Graph()
b5.add_weighted_edges_from([
                            (1,2,4),
                            (1,3,8),
                            (2,3,11),
                            (2,4,8),
                            (3,6,7),
                            (3,7,1),
                            (6,4,2),
                            (6,7,20),
                            (7,8,2),
                            (4,8,4),
                            (5,8,14),
                            (5,9,9),
                            (8,9,10),
                            (4,5,7)
                            ])
b6 = kr()
b7 = b6.kruskal(b5)
print(b7.edges)
print(b6.peso(b7))