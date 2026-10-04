import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def fonk1(vertices, keys, heap):
    b1 = {}
    for vertex in vertices:
        b1[vertex] = heap.insert(keys[vertex], vertex)
    return b1
def fonk2():
    b2 = nx.Graph()
    b3 = {
        'a': (0, 1),
        'b': (2, 1),
        'c': (1, 0),
        'd': (1, 2)
    }
    for node, position in b3.items():
        b2.add_node(node, b4 = position, key=0)
    b5 = [
        ('a', 'b', 2),
        ('a', 'c', 30),
        ('b', 'c', 90),
        ('d', 'b', 1),
        ('d', 'a', 3)
    ]
    for v1, v2, b6 in b5:
        b2.add_edge(v1, v2, b6 = b6)
    return b2
def fonk3(b2, b13, b10):
    plt.figure(b7 = (12, 6))
    plt.subplot(121)
    nx.draw(b2, b4 = b10, with_labels=True)
    b8 = nx.get_edge_attributes(b2, 'b6')
    nx.draw_networkx_edge_labels(b2, b4 = b10, edge_labels=b8)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(b13, b4 = b10, with_labels=True)
    b9 = nx.get_edge_attributes(b13, 'b6')
    nx.draw_networkx_edge_labels(b13, b4 = b10, edge_labels=b9)
    plt.title("Minimum Spanning Tree (b13)")
    plt.show()
def fonk4():
    b2 = fonk2()
    b10 = nx.get_node_attributes(b2, 'b4')
    b11 = 'a'
    b12 = set(b2.b3())
    b8 = nx.get_edge_attributes(b2, 'b6')
    b13 = prim(b2, b8, b11, b12)
    fonk3(b2, b13, b10)
if b14 = = "__main__":
    fonk4()