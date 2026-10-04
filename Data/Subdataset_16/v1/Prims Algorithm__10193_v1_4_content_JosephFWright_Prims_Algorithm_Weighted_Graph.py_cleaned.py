import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b2 = dict()
        b3 = np.loadtxt(self.b1, int)
        for row in b3:
            b2[(row[0], row[1])] = row[2]
        return b2
    def fonk3(self):
        return set(self.fonk2().keys())
    def fonk4(self):
        b4 = set()
        for b6 in self.fonk3():
            for v in b6:
                b4.add(v)
        return b4
    def fonk5(self):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b6 = [(u, v) for (u, v, d) in b5.edges(data=True)]
        b7 = nx.spring_layout(b5, seed=7)
        nx.draw_networkx_nodes(b5, b7, b8 = 250)
        nx.draw_networkx_edges(b5, b7, b9 = b6, width=1)
        b10 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b7, b11 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b7, b12 = b10)
        plt.axis('off')
        plt.show()
    def fonk6(self, H):
        b5 = nx.read_edgelist(self.b1, nodetype=int, data=(('weight', float),))
        b13 = [(u, v) for (u, v, d) in b5.edges(data=True)]
        b14 = [b6 for b6 in b13 if b6 in H[1]]
        b15 = [v for v in H[0]]
        b7 = nx.spring_layout(b5, seed=7)
        nx.draw_networkx_nodes(b5, b7, b8 = 250)
        nx.draw_networkx_nodes(b5, b7, b16 = b15, b8=400)
        nx.draw_networkx_edges(b5, b7, b9 = b13, width=1)
        nx.draw_networkx_edges(b5, b7, b9 = b14, edge_color="r", width=3)
        b10 = nx.get_edge_attributes(b5, 'weight')
        nx.draw_networkx_labels(b5, b7, b11 = 10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(b5, b7, b12 = b10)
        plt.axis('off')
        plt.show()
