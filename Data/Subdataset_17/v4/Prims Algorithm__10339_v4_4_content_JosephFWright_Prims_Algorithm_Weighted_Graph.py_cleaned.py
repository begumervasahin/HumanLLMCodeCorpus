import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class WeightedGraph:
    def __init__(self, edge_list_file):
        self.edge_list_file = edge_list_file
    def edge_dict(self):
        edge_dict = {}
        edge_list = np.loadtxt(self.edge_list_file, dtype=int)
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]
        return edge_dict
    def edge_set(self):
        return set(self.edge_dict().keys())
    def vertex_set(self):
        vertex_set = set()
        for edge in self.edge_set():
            vertex_set.update(edge)
        return vertex_set
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
    def draw_subgraph(self, H):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        pos = nx.spring_layout(G, seed=7)
        all_edges = [(u, v) for (u, v, d) in G.edges(data=True)]
        subgraph_edges = [e for e in all_edges if e in H[1]]
        subgraph_nodes = list(H[0])
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_nodes(G, pos, nodelist=subgraph_nodes, node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=all_edges, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=subgraph_edges, edge_color="r", width=3)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()