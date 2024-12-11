
from algorithm import Graph, prim
b1 = Graph()
b2 = [
    ('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8),
    ('c', 'd', 7), ('b', 'h', 11), ('h', 'i', 7),
    ('i', 'c', 2), ('i', 'g', 6), ('h', 'g', 1),
    ('g', 'f', 2), ('c', 'f', 4), ('d', 'f', 14),
    ('d', 'e', 9), ('f', 'e', 10)
]
for edge in b2:
    b1.add_directed_edge(*edge)
b3 = 'a'
b4 = prim(b1, b3)