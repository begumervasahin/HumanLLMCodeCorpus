import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap_mod import FibonacciHeap
from prim_algorithm import prim
def build_heap(vertices, key_dict, heap):
    nodes_heap = {}
    for vertex in vertices:
        nodes_heap[vertex] = heap.insert(key_dict[vertex], vertex)
    return nodes_heap
def main():
    G = nx.Graph()
    node_positions = {
        'a': (0, 1),
        'b': (2, 1),
        'c': (1, 0),
        'd': (1, 2)
    }
    for node, pos in node_positions.items():
        G.add_node(node, pos=pos, key=0)
    edges_with_weights = [
        ('a', 'b', 2),
        ('a', 'c', 30),
        ('b', 'c', 90),
        ('d', 'b', 1),
        ('d', 'a', 3)
    ]
    G.add_weighted_edges_from(edges_with_weights)
    edge_weights = nx.get_edge_attributes(G, 'weight')
    node_positions = nx.get_node_attributes(G, 'pos')
    start_node = 'a'
    node_set = G.nodes()
    mst = prim(G, edge_weights, start_node, node_set)
    mst_edges = mst.edges()
    mst_edge_weights = nx.get_edge_attributes(mst, 'weight')
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    nx.draw(G, node_positions, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_weights)
    plt.title("Original Graph")
    plt.subplot(122)
    nx.draw(mst, node_positions, with_labels=True, node_color='lightgreen', edge_color='black')
    nx.draw_networkx_edge_labels(mst, node_positions, edge_labels=mst_edge_weights)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()
if __name__ == "__main__":
    main()