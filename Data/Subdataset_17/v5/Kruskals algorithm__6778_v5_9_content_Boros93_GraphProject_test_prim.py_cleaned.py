import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_heap(vertices, keys, heap):
    nodes_in_heap = {}
    for vertex in vertices:
        nodes_in_heap[vertex] = heap.insert(keys[vertex], vertex)
    return nodes_in_heap
def initialize_graph():
    G = nx.Graph()
    nodes = {
        'a': (0, 1),
        'b': (2, 1),
        'c': (1, 0),
        'd': (1, 2)
    }
    for node, position in nodes.items():
        G.add_node(node, pos=position, key=0)
    edges = [
        ('a', 'b', 2),
        ('a', 'c', 30),
        ('b', 'c', 90),
        ('d', 'b', 1),
        ('d', 'a', 3)
    ]
    for v1, v2, weight in edges:
        G.add_edge(v1, v2, weight=weight)
    return G
def plot_graphs(G, MST, node_positions):
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    nx.draw(G, pos=node_positions, with_labels=True)
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(MST, pos=node_positions, with_labels=True)
    mst_edge_weights = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos=node_positions, edge_labels=mst_edge_weights)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()
def main():
    G = initialize_graph()
    node_positions = nx.get_node_attributes(G, 'pos')
    start_node = 'a'
    node_set = set(G.nodes())
    edge_weights = nx.get_edge_attributes(G, 'weight')
    MST = prim(G, edge_weights, start_node, node_set)
    plot_graphs(G, MST, node_positions)
if __name__ == "__main__":
    main()