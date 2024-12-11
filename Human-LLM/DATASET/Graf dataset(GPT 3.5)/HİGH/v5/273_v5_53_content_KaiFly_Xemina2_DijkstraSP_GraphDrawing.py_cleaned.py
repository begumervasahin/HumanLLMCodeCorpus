import matplotlib.pyplot as plt
import networkx as nx
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = nx.DiGraph()
        self.b3 = b1.number_vertexes()
    def fonk2(self, b4 = None):
        for edge in self.b1.edges:
            self.b2.add_edge(edge[0], edge[1], b5 = self.b1.weights[edge])
        if b4 is None:
            b4 = nx.spring_layout(self.b2, k=0.3 * 1 / math.sqrt(self.b3), iterations=50, scale=1.0)
        b6 = {(u, v): d['b5'] for u, v, d in self.b2.edges(data=True)}
        b7 = [d['b5'] for (_, _, d) in self.b2.edges(data=True)]
        b8 = {node: node for node in self.b2.nodes()}
        a1 = 8
        if self.b3 >= 10:
            b7 = [w / (math.sqrt(self.b3) * 4) for w in b7]
            a1 = 8 / (math.sqrt(self.b3))
        nx.draw_networkx_nodes(self.b2, b4, b9 = 'green', node_size=50, b12=12)
        nx.draw_networkx_edge_labels(self.b2, b4, b10 = 0.3, b12=a1, font_color='black', b6=b6)
        nx.draw_networkx_edges(self.b2, b4, b11 = b7, edge_color='blue')
        nx.draw_networkx_labels(self.b2, b4, b12 = 5, font_color='black', labels=b8)
        plt.plot()
        return b4
    def fonk3(self, path, b4 = None):
        for edge in self.b1.edges:
            self.b2.add_edge(edge[0], edge[1], b5 = self.b1.weights[edge])
        if b4 is None:
            b4 = nx.spring_layout(self.b2)
        b6 = {(u, v): d['b5'] for u, v, d in self.b2.edges(data=True)}
        b7 = [d['b5'] for (_, _, d) in self.b2.edges(data=True)]
        b13 = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        b14 = ['blue' if edge not in b13 else 'red' for edge in self.b2.edges()]
        b8 = {node: node for node in self.b2.nodes()}
        a1 = 8
        if self.b3 >= 10:
            b7 = [w / math.sqrt(self.b3) for w in b7]
            a1 = 8 / math.sqrt(self.b3)
        nx.draw_networkx_nodes(self.b2, b4, b9 = 'green', node_size=50, b12=12)
        nx.draw_networkx_edge_labels(self.b2, b4, b12 = a1, b10=0.3, font_color='black', b6=b6)
        nx.draw_networkx_edges(self.b2, b4, b11 = b7, edge_color=b14)
        nx.draw_networkx_edges(self.b2, b4, b11 = max(b7), edgelist=b13, edge_color='red')
        nx.draw_networkx_labels(self.b2, b4, b12 = 5, font_color='black', labels=b8)
        return b4