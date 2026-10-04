import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b2 = {}
        b3 = np.loadtxt(self.b1, int)
        for row in b3:
            b2[(row[0], row[1])] = row[2]
        return b2
    def fonk3(self):
        return set(self.fonk2().keys())
    def fonk4(self):
        b4 = set()
        for edge in self.fonk3():
            b4.update(edge)
        return b4
    def fonk5(self):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = nx.spring_layout(b5, seed=7)
        nx.draw_networkx_nodes(b5, b6, b7 = 250)
        nx.draw_networkx_edges(b5, b6, b8 = 1)
        b9 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_edge_labels(b5, b6, b9 = b9)
        nx.draw_networkx_labels(b5, b6, b10 = 10, font_family='sans-serif')
        plt.axis('off')
        plt.show()
    def fonk6(self, subgraph):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = nx.spring_layout(b5, seed=7)
        nx.draw_networkx_nodes(b5, b6, b7 = 250)
        nx.draw_networkx_nodes(b5, b6, b11 = list(subgraph[0]), b7=400, node_color='red')
        b12 = list(b5.edges(data=True))
        b13 = [edge for edge in b12 if (edge[0], edge[1]) in subgraph[1]]
        nx.draw_networkx_edges(b5, b6, b14 = b12, b8=1)
        nx.draw_networkx_edges(b5, b6, b14 = b13, edge_color='red', b8=3)
        b9 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_edge_labels(b5, b6, b9 = b9)
        nx.draw_networkx_labels(b5, b6, b10 = 10, font_family='sans-serif')
        plt.axis('off')
        plt.show()
