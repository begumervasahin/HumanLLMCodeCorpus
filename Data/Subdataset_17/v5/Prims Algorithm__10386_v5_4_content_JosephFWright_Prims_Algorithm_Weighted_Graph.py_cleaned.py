import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class WeightedGraph:
    def __init__(self, edge_list_file):
        self.edge_list_file = edge_list_file
    def load_edge_list(self):
        return np.loadtxt(self.edge_list_file, dtype=int)
    def edge_dict(self):
        edge_list = self.load_edge_list()
        return {(row[0], row[1]): row[2] for row in edge_list}
    def edge_set(self):
        return set(self.edge_dict().keys())
    def vertex_set(self):
        vertices = set()
        for edge in self.edge_set():
            vertices.update(edge)
        return vertices
    def draw_graph(self):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_edges(G, pos, width=1)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
    def draw_subgraph(self, subgraph):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        pos = nx.spring_layout(G, seed=7)
        all_edges = [(u, v) for u, v, d in G.edges(data=True)]
        subgraph_edges = [e for e in all_edges if e in subgraph[1]]
        subgraph_nodes = list(subgraph[0])
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_nodes(G, pos, nodelist=subgraph_nodes, node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=all_edges, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=subgraph_edges, edge_color="r", width=3)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
