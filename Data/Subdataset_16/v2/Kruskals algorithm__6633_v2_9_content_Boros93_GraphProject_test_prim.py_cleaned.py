import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap_mod import FibonacciHeap
from prim_algorithm import prim
def fonk1(vertices, key_dict, heap):
    b1 = {}
    for vertex in vertices:
        b1[vertex] = heap.insert(key_dict[vertex], vertex)
    return b1
def fonk2():
    b2 = nx.Graph()
    b3 = {
        'a': (0, 1),
        'b': (2, 1),
        'c': (1, 0),
        'd': (1, 2)
    }
    for node, b4 in b3.items():
        b2.add_node(node, b4 = b4, key=0)
    b5 = [
        ('a', 'b', 2),
        ('a', 'c', 30),
        ('b', 'c', 90),
        ('d', 'b', 1),
        ('d', 'a', 3)
    ]
    for u, v, b6 in b5:
        b2.add_edge(u, v, b6 = b6)
    b7 = nx.get_edge_attributes(b2, 'b6')
    b3 = nx.get_node_attributes(b2, 'b4')
    b8 = 'a'
    b9 = b3.keys()
    b10 = prim(b2, b7, b8, b9)
    b11 = b10.edges()
    b12 = nx.get_edge_attributes(b10, 'b6')
    plt.figure(b13 = (10, 5))
    plt.subplot(121)
    nx.draw(b2, b3, b14 = True)
    nx.draw_networkx_edge_labels(b2, b3, b15 = b7)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(b10, b3, b14 = True)
    nx.draw_networkx_edge_labels(b10, b3, b15 = b12)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()
if b16 = = "__main__":
    fonk2()