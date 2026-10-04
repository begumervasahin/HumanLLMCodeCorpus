import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class Weighted_Graph(object):
    def __init__(self, edge_list_file):
        self.edge_list_file = edge_list_file
    def edge_dict(self):
        edge_dict = dict()
        edge_list = np.loadtxt(self.edge_list_file, int)
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]
        return edge_dict
    def edge_set(self):
        return set(self.edge_dict().keys())
    def vertex_set(self):
        vertex_set = set()
        for e in self.edge_set():
            for v in e:
                vertex_set.add(v)
        return vertex_set
    def draw_graph(self):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        e = [(u, v) for (u, v, d) in G.edges(data=True)]
        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_edges(G, pos, edgelist=e, width=1)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
    def draw_subgraph(self, H):
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight', float),))
        e1 = [(u, v) for (u, v, d) in G.edges(data=True)]
        e2 = [e for e in e1 if e in H[1]]
        v1 = [v for v in H[0]]
        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=250)
        nx.draw_networkx_nodes(G, pos, nodelist=v1, node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=e1, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=e2, edge_color="r", width=3)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()
