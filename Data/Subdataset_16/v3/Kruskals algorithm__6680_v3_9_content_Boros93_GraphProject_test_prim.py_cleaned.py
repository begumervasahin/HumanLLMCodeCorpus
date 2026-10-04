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
    b2.add_weighted_edges_from(b5)
    b6 = nx.get_edge_attributes(b2, 'weight')
    b3 = nx.get_node_attributes(b2, 'b4')
    b7 = 'a'
    b8 = b2.nodes()
    b9 = prim(b2, b6, b7, b8)
    b10 = b9.edges()
    b11 = nx.get_edge_attributes(b9, 'weight')
    plt.figure(b12 = (12, 6))
    plt.subplot(121)
    nx.draw(b2, b3, b13 = True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(b2, b3, b14 = b6)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(b9, b3, b13 = True, node_color='lightgreen', edge_color='black')
    nx.draw_networkx_edge_labels(b9, b3, b14 = b11)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()
if b15 = = "__main__":
    fonk2()