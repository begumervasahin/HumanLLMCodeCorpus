
from dijkstra import Graph, get_dijkstra_path
def fonk1():
    b1 = Graph()
    b2 = [
        ('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8), ('c', 'd', 7),
        ('b', 'h', 11), ('h', 'i', 7), ('i', 'c', 2), ('i', 'g', 6),
        ('h', 'g', 1), ('g', 'f', 2), ('c', 'f', 4), ('d', 'f', 14),
        ('d', 'e', 9), ('f', 'e', 10)
    ]
    for from_node, to_node, weight in b2:
        b1.add_directed_edge(from_node, to_node, weight)
    return b1
def fonk2():
    b1 = Graph()
    b2 = [
        ('s', 't', 10), ('s', 'y', 5), ('t', 'x', 1), ('y', 'z', 2),
        ('t', 'y', 2), ('y', 't', 3), ('x', 'z', 4), ('z', 'x', 6),
        ('y', 'x', 9), ('z', 's', 7)
    ]
    for node1, node2, weight in b2:
        b1.add_undirected_edge(node1, node2, weight)
    return b1
def fonk3():
    b3 = fonk1()
    b4 = fonk2()
    b5 = get_dijkstra_path(b4, 't', 's')
    print(f"The shortest b5 from 't' to 's' is: {b5}")
if b6 = = "__main__":
    fonk3()