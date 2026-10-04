import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return np.loadtxt(self.b1, b2 = int)
    def fonk3(self):
        b3 = self.fonk2()
        return {(row[0], row[1]): row[2] for row in b3}
    def fonk4(self):
        return set(self.fonk3().keys())
    def fonk5(self):
        b4 = set()
        for edge in self.fonk4():
            b4.update(edge)
        return b4
    def fonk6(self):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = nx.spring_layout(b5, seed=7)
        nx.draw_networkx_nodes(b5, b6, b7 = 250)
        nx.draw_networkx_edges(b5, b6, b8 = 1)
        b9 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b6, b10 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b6, b11 = b9)
        plt.axis('off')
        plt.show()
    def fonk7(self, subgraph):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = nx.spring_layout(b5, seed=7)
        b12 = [(u, v) for u, v, d in b5.edges(data=True)]
        b13 = [e for e in b12 if e in subgraph[1]]
        b14 = list(subgraph[0])
        nx.draw_networkx_nodes(b5, b6, b7 = 250)
        nx.draw_networkx_nodes(b5, b6, b15 = b14, b7=400)
        nx.draw_networkx_edges(b5, b6, b16 = b12, b8=1)
        nx.draw_networkx_edges(b5, b6, b16 = b13, edge_color="r", b8=3)
        b9 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b6, b10 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b6, b11 = b9)
        plt.axis('off')
        plt.show()
