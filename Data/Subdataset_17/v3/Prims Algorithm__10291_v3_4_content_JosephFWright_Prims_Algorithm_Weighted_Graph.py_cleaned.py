import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class WeightedGraph:
    def __init__(self, edge_list_file):
        self.edge_list_file = edge_list_file
    def edge_dict(self):
        edge_dict = {}
        edge_list = np.loadtxt(self.edge_list_file, int)
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]
        return edge_dict
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
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.axis('off')
        plt.show()
    def draw_subgraph(self, subgraph):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_nodes(G, pos, nodelist=list(subgraph[0]), node_size=400, node_color='red')
        all_edges = list(G.edges(data=True))
        highlighted_edges = [edge for edge in all_edges if (edge[0], edge[1]) in subgraph[1]]
        nx.draw_networkx_edges(G, pos, edgelist=all_edges, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, edge_color='red', width=3)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.axis('off')
        plt.show()
