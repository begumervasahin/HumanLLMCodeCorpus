import networkx as nx
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim
def build_heap(vertices, keys, heap):
    node_heap_mapping = {}
    for vertex in vertices:
        node_heap_mapping[vertex] = heap.insert(keys[vertex], vertex)
    return node_heap_mapping
graph = nx.Graph()
node_set = ('a', 'b', 'c', 'd')
graph.add_node('a', pos=(0, 1), key=0)
graph.add_node('b', pos=(2, 1), key=0)
graph.add_node('c', pos=(1, 0), key=0)
graph.add_node('d', pos=(1, 2), key=0)
graph.add_edge('a', 'b', weight=2)
graph.add_edge('a', 'c', weight=30)
graph.add_edge('b', 'c', weight=90)
graph.add_edge('d', 'b', weight=1)
graph.add_edge('d', 'a', weight=3)
edge_weights = nx.get_edge_attributes(graph, 'weight')
node_positions = nx.get_node_attributes(graph, 'pos')
edges = graph.edges
starting_node = 'a'
minimum_spanning_tree = prim(graph, edge_weights, starting_node, node_set)
mst_edges = minimum_spanning_tree.edges()
mst_edge_weights = nx.get_edge_attributes(minimum_spanning_tree, 'weight')
plt.subplot(121)
nx.draw(graph, node_positions, with_labels=True)
nx.draw_networkx_edge_labels(graph, node_positions, edge_labels=edge_weights)
nx.draw(graph, node_positions, edges=edges)
plt.subplot(122)
nx.draw(minimum_spanning_tree, node_positions, with_labels=True)
nx.draw_networkx_edge_labels(minimum_spanning_tree, node_positions, edge_labels=mst_edge_weights)
nx.draw(minimum_spanning_tree, node_positions, edges=mst_edges)
plt.show()