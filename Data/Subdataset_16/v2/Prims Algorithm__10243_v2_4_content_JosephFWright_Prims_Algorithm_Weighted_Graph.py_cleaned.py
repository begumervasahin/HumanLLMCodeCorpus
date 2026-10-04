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
        b7 = list(b5.b7(data=True))
        nx.draw_networkx_nodes(b5, b6, b8 = 250)
        nx.draw_networkx_edges(b5, b6, b9 = b7, width=1)
        b10 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b6, b11 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b6, b12 = b10)
        plt.axis('off')
        plt.show()
    def fonk6(self, subgraph):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = nx.spring_layout(b5, seed=7)
        b13 = list(b5.b7(data=True))
        b14 = [edge for edge in b13 if edge[:2] in subgraph[1]]
        nx.draw_networkx_nodes(b5, b6, b8 = 250)
        nx.draw_networkx_nodes(b5, b6, b15 = list(subgraph[0]), b8=400)
        nx.draw_networkx_edges(b5, b6, b9 = b13, width=1)
        nx.draw_networkx_edges(b5, b6, b9 = b14, edge_color="r", width=3)
        b10 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b6, b11 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b6, b12 = b10)
        plt.axis('off')
        plt.show()
