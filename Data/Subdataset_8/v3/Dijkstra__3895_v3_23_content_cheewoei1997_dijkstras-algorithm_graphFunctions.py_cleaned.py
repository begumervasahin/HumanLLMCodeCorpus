from collections import namedtuple, deque
import matplotlib.pyplot as plt
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])
class Graph:
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in self.edges), []))
    def dijkstra(self, source, dest):
        assert source in self.vertices
        distances = {vertex: inf for vertex in self.vertices}
        previous_nodes = {vertex: None for vertex in self.vertices}
        distances[source] = 0
        remaining_vertices = self.vertices.copy()
        neighbors = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbors[start].add((end, cost))
        while remaining_vertices:
            current_vertex = min(remaining_vertices, key=lambda vertex: distances[vertex])
            remaining_vertices.remove(current_vertex)
            if distances[current_vertex] == inf or current_vertex == dest:
                break
            for neighbor, cost in neighbors[current_vertex]:
                new_distance = distances[current_vertex] + cost
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_vertex
        shortest_path = deque()
        current_node = dest
        while previous_nodes[current_node]:
            shortest_path.appendleft(current_node)
            current_node = previous_nodes[current_node]
        shortest_path.appendleft(current_node)
        return shortest_path
def draw_graph(edges, total_nodes, shortest_path, start_nodes, end_nodes, weights):
    G = nx.DiGraph()
    path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    for i in range(total_nodes):
        G.add_edge(start_nodes[i], end_nodes[i], weight=weights[i])
    edge_labels = {edge: weight for edge, weight in zip(edges, weights)}
    pos = nx.nx_pydot.graphviz_layout(G, prog='neato')
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500,
            node_color='pink', labels={node: node for node in G.nodes()}, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', arrows=True, arrowsize=24)
    nx.draw_networkx_edges(G, pos, edgelist=[edge for edge in G.edges() if edge not in path_edges], arrows=False)
    plt.axis('off')
    plt.show()
def swap_nodes(start_nodes, end_nodes, weights):
    return start_nodes + end_nodes, end_nodes + start_nodes, weights + weights
edges = [(1, 2, 5), (2, 3, 7), (1, 3, 10), (2, 4, 3), (3, 4, 1)]
graph = Graph(edges)
start_nodes = [1, 2, 1, 2, 3]
end_nodes = [2, 3, 3, 4, 4]
weights = [5, 7, 10, 3, 1]
total_nodes = len(start_nodes)
source_node = 1
dest_node = 4
shortest_path = graph.dijkstra(source_node, dest_node)
draw_graph(edges, total_nodes, shortest_path, start_nodes, end_nodes, weights)