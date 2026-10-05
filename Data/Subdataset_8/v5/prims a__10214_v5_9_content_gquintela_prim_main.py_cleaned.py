
from algorithm import Graph, prim
graph = Graph()
edges = [
    ('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8),
    ('c', 'd', 7), ('b', 'h', 11), ('h', 'i', 7),
    ('i', 'c', 2), ('i', 'g', 6), ('h', 'g', 1),
    ('g', 'f', 2), ('c', 'f', 4), ('d', 'f', 14),
    ('d', 'e', 9), ('f', 'e', 10)
]
for edge in edges:
    graph.add_directed_edge(*edge)
start_node = 'a'
minimum_spanning_tree = prim(graph, start_node)