import matplotlib.pyplot as plt
import networkx as nx
import math
from Dijkstra_3a import Graph
from test_complexity import dijkstra
class GraphDrawing:
    def __init__(self, graph):
        self.graph = graph
        self.graph_networkx = nx.DiGraph()
        self.num_vertices = graph.number_vertexes()
    def draw_graph(self, pos=None):
        for i in range(self.graph.number_edges()):
            self.graph_networkx.add_edge(self.graph.edges[i][0], self.graph.edges[i][1], weight=self.graph.weights[i])
        if pos is None:
            pos = nx.spring_layout(self.graph_networkx, k=0.3*1/math.sqrt(self.num_vertices), iterations=50, scale=1.0)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.graph_networkx.edges(data=True)}
        edge_widths = [d['weight'] for (_, _, d) in self.graph_networkx.edges(data=True)]
        node_labels = {node: node for node in self.graph_networkx.nodes()}
        font_label_size = 8
        if self.num_vertices >= 10:
            scaling_factor = 1 / math.sqrt(self.num_vertices)
            edge_widths = [w / (4 * scaling_factor) for w in edge_widths]
            font_label_size = 8 * scaling_factor
        nx.draw_networkx_nodes(self.graph_networkx, pos, node_color='green', node_size=50, font_size=12)
        nx.draw_networkx_edge_labels(self.graph_networkx, pos, label_pos=0.3, font_size=font_label_size, font_color='black', edge_labels=edge_labels)
        nx.draw_networkx_edges(self.graph_networkx, pos, width=edge_widths, edge_color='blue')
        nx.draw_networkx_labels(self.graph_networkx, pos, font_size=5, font_color='black', labels=node_labels)
        plt.plot()
        return pos
    def draw_path(self, path, pos=None):
        for i in range(self.graph.number_edges()):
            self.graph_networkx.add_edge(self.graph.edges[i][0], self.graph.edges[i][1], weight=self.graph.weights[i])
        if pos is None:
            pos = nx.spring_layout(self.graph_networkx)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.graph_networkx.edges(data=True)}
        edge_widths = [d['weight'] for (_, _, d) in self.graph_networkx.edges(data=True)]
        red_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        edge_colors = ['blue' if edge not in red_edges else 'red' for edge in self.graph_networkx.edges()]
        node_labels = {node: node for node in self.graph_networkx.nodes()}
        font_label_size = 8
        if self.num_vertices >= 10:
            scaling_factor = 1 / math.sqrt(self.num_vertices)
            edge_widths = [w / scaling_factor for w in edge_widths]
            font_label_size = 8 * scaling_factor
        nx.draw_networkx_nodes(self.graph_networkx, pos, node_color='green', node_size=50, font_size=12)
        nx.draw_networkx_edge_labels(self.graph_networkx, pos, font_size=font_label_size, label_pos=0.3, font_color='black', edge_labels=edge_labels)
        nx.draw_networkx_edges(self.graph_networkx, pos, width=edge_widths, edge_color=edge_colors)
        nx.draw_networkx_edges(self.graph_networkx, pos, width=max(edge_widths), edgelist=red_edges, edge_color='red')
        nx.draw_networkx_labels(self.graph_networkx, pos, font_size=5, font_color='black', labels=node_labels)
        return pos
graph_drawer = GraphDrawing(graph)
graph_drawer.draw_graph()
graph_drawer.draw_path(path)