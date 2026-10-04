import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
def build_heap(nodes, keys, heap):
    nodes_heap = {}
    for node in nodes:
        nodes_heap[node] = heap.insert(keys[node], node)
    return nodes_heap
def initialize_graph():
    G = nx.Graph()
    node_positions = {
        'a': (0, 2),
        'b': (1, 0),
        'c': (2, 2),
        'd': (3, 0)
    }
    for node, pos in node_positions.items():
        G.add_node(node, pos=pos, key=math.inf, pred=None, flag=False)
    edges = [
        ('a', 'b', 2),
        ('a', 'c', 10),
        ('b', 'c', 9),
        ('b', 'd', 1),
        ('d', 'a', 3)
    ]
    G.add_weighted_edges_from(edges)
    return G
def draw_graph(G, pos, subplot_index, title):
    plt.subplot(subplot_index)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
def prim_mst(G, start_node):
    G.nodes[start_node]['key'] = 0
    heap = FibonacciHeap()
    keys = nx.get_node_attributes(G, 'key')
    nodes_heap = build_heap(G.nodes, keys, heap)
    while heap.total_nodes != 0:
        u = heap.extract_min().value
        G.nodes[u]['flag'] = True
        for v in G.neighbors(u):
            if not G.nodes[v]['flag'] and G[u][v]['weight'] < G.nodes[v]['key']:
                G.nodes[v]['key'] = G[u][v]['weight']
                G.nodes[v]['pred'] = u
                heap.decrease_key(nodes_heap[v], G[u][v]['weight'])
    MST = nx.Graph()
    for node in G.nodes:
        pred = G.nodes[node]['pred']
        if pred is not None:
            MST.add_edge(pred, node, weight=G[pred][node]['weight'])
    return MST
G = initialize_graph()
positions = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(12, 6))
draw_graph(G, positions, 121, 'Initial Graph')
start_node = 'a'
MST = prim_mst(G, start_node)
draw_graph(MST, positions, 122, 'Minimum Spanning Tree')
plt.show()