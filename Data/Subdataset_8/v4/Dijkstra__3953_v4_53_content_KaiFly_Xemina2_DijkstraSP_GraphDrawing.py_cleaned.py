import matplotlib.pyplot as plt
import networkx as nx
import math
class GraphDrawing:
    def __init__(self, graph):
        self.G = graph
        self.Gx = nx.DiGraph()
        self.len = graph.number_vertexes()
    def draw_graph(self, pos=None):
        for i in range(self.G.number_edges()):
            self.Gx.add_edge(self.G.edges[i][0], self.G.edges[i][1], weight=self.G.weights[i])
        if pos is None:
            pos = nx.spring_layout(self.Gx, k=0.3 * 1 / math.sqrt(self.len), iterations=50, scale=1.0)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.Gx.edges(data=True)}
        edge_widths = [d['weight'] for (_, _, d) in self.Gx.edges(data=True)]
        node_labels = {node: node for node in self.Gx.nodes()}
        font_label_size = 8
        if self.len >= 10:
            n = self.len
            edge_widths = [i / (math.sqrt(n) * 4) for i in edge_widths]
            font_label_size = 8 / (math.sqrt(n))
        nx.draw_networkx_nodes(self.Gx, pos, node_color='green', node_size=50, font_size=12)
        nx.draw_networkx_edge_labels(self.Gx, pos, label_pos=0.3, font_size=font_label_size, font_color='black', edge_labels=edge_labels)
        nx.draw_networkx_edges(self.Gx, pos, width=edge_widths, edge_color='blue')
        nx.draw_networkx_labels(self.Gx, pos, font_size=5, font_color='black', labels=node_labels)
        plt.plot()
        return pos
    def draw_path(self, path, pos=None):
        for i in range(self.G.number_edges()):
            self.Gx.add_edge(self.G.edges[i][0], self.G.edges[i][1], weight=self.G.weights[i])
        if pos is None:
            pos = nx.spring_layout(self.Gx)
        edge_labels = {(u, v): d['weight'] for u, v, d in self.Gx.edges(data=True)}
        edge_widths = [d['weight'] for (_, _, d) in self.Gx.edges(data=True)]
        red_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        edge_colors = ['blue' if edge not in red_edges else 'red' for edge in self.Gx.edges()]
        node_labels = {node: node for node in self.Gx.nodes()}
        font_label_size = 8
        if self.len >= 10:
            n = self.len
            edge_widths = [i / math.sqrt(n) for i in edge_widths]
            font_label_size = 8 / math.sqrt(n)
        nx.draw_networkx_nodes(self.Gx, pos, node_color='green', node_size=50, font_size=12)
        nx.draw_networkx_edge_labels(self.Gx, pos, font_size=font_label_size, label_pos=0.3, font_color='black', edge_labels=edge_labels)
        nx.draw_networkx_edges(self.Gx, pos, width=edge_widths, edge_color=edge_colors)
        nx.draw_networkx_edges(self.Gx, pos, width=max(edge_widths), edgelist=red_edges, edge_color='red')
        nx.draw_networkx_labels(self.Gx, pos, font_size=5, font_color='black', labels=node_labels)
        return pos