import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def draw_graph(graph, export=False, name='graph'):
    tmp_graph = graph.copy()
    for node in tmp_graph.nodes():
        tmp_graph.node[node]['label'] = node
    pos = nx.spring_layout(tmp_graph)
    nx.draw(tmp_graph, pos)
    node_labels = nx.get_node_attributes(tmp_graph, 'label')
    nx.draw_networkx_labels(tmp_graph, pos, labels=node_labels)
    if export:
        plt.savefig(name + '.png')
    else:
        plt.show()
    plt.close()
def dijkstra(graph, sources):
    tmp_graph = graph.copy()
    push = heappush
    pop = heappop
    for node in tmp_graph.nodes():
        tmp_graph.node[node]['lambda'] = np.inf
        tmp_graph.node[node]['pi'] = None
    for source in sources:
        tmp_graph.node[source]['lambda'] = 0
    q = []
    visited = []
    for node in tmp_graph.nodes():
        push(q, (tmp_graph.node[node]['lambda'], node))
    while q:
        u = pop(q)
        u = u[1]
        visited.append(u)
        for v in tmp_graph.neighbors(u):
            if v not in visited and tmp_graph.node[v]['lambda'] > (tmp_graph.node[u]['lambda'] + tmp_graph[u][v]['weight']):
                q.remove((tmp_graph.node[v]['lambda'], v))
                tmp_graph.node[v]['lambda'] = tmp_graph.node[u]['lambda'] + tmp_graph[u][v]['weight']
                push(q, (tmp_graph.node[v]['lambda'], v))
                tmp_graph.node[v]['pi'] = u
    shortest_path_tree = nx.Graph()
    for u in tmp_graph.nodes():
        shortest_path_tree.add_node(u)
        if tmp_graph.node[u]['pi'] is not None:
            shortest_path_tree.add_edge(u, tmp_graph.node[u]['pi'])
            shortest_path_tree[u][tmp_graph.node[u]['pi']]['weight'] = tmp_graph[u][tmp_graph.node[u]['pi']]['weight']
    return shortest_path_tree
def read_weighted_adjacency_matrix(path):
    data = np.loadtxt(path)
    rows, cols = np.where(data > 0)
    edges = zip(rows, cols)
    g = nx.Graph(edges)
    for u, v in zip(rows, cols):
        g[u][v]['weight'] = data[u][v]
    return g
input_file = "adjacentes1.txt"
graph = read_weighted_adjacency_matrix(input_file)
source_nodes = []
execution_times = []
for _ in range(10):
    start_time = timeit.default_timer()
    dijkstra(graph, source_nodes)
    end_time = timeit.default_timer()
    execution_times.append((end_time - start_time) / 10.0)
print(sum(execution_times))