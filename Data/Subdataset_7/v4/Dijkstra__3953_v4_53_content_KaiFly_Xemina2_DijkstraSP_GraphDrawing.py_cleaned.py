import matplotlib.pyplot as plt
import networkx as nx
import math
class class1:
    def fonk1(self, graph):
        self.b1 = graph
        self.b2 = nx.DiGraph()
        self.b3 = graph.number_vertexes()
    def fonk2(self, b4 = None):
        for i in range(self.b1.number_edges()):
            self.b2.add_edge(self.b1.edges[i][0], self.b1.edges[i][1], b5 = self.b1.weights[i])
        if b4 is None:
            b4 = nx.spring_layout(self.b2, k=0.3 * 1 / math.sqrt(self.b3), iterations=50, scale=1.0)
        b6 = {(u, v): d['b5'] for u, v, d in self.b2.edges(data=True)}
        b7 = [d['b5'] for (_, _, d) in self.b2.edges(data=True)]
        b8 = {node: node for node in self.b2.nodes()}
        a1 = 8
        if self.b3 >= 10:
            b9 = self.b3
            b7 = [i / (math.sqrt(b9) * 4) for i in b7]
            a1 = 8 / (math.sqrt(b9))
        nx.draw_networkx_nodes(self.b2, b4, b10 = 'green', node_size=50, b13=12)
        nx.draw_networkx_edge_labels(self.b2, b4, b11 = 0.3, b13=a1, font_color='black', b6=b6)
        nx.draw_networkx_edges(self.b2, b4, b12 = b7, edge_color='blue')
        nx.draw_networkx_labels(self.b2, b4, b13 = 5, font_color='black', labels=b8)
        plt.plot()
        return b4
    def fonk3(self, path, b4 = None):
        for i in range(self.b1.number_edges()):
            self.b2.add_edge(self.b1.edges[i][0], self.b1.edges[i][1], b5 = self.b1.weights[i])
        if b4 is None:
            b4 = nx.spring_layout(self.b2)
        b6 = {(u, v): d['b5'] for u, v, d in self.b2.edges(data=True)}
        b7 = [d['b5'] for (_, _, d) in self.b2.edges(data=True)]
        b14 = [(path[i], path[i + 1]) for i in range(b3(path) - 1)]
        b15 = ['blue' if edge not in b14 else 'red' for edge in self.b2.edges()]
        b8 = {node: node for node in self.b2.nodes()}
        a1 = 8
        if self.b3 >= 10:
            b9 = self.b3
            b7 = [i / math.sqrt(b9) for i in b7]
            a1 = 8 / math.sqrt(b9)
        nx.draw_networkx_nodes(self.b2, b4, b10 = 'green', node_size=50, b13=12)
        nx.draw_networkx_edge_labels(self.b2, b4, b13 = a1, b11=0.3, font_color='black', b6=b6)
        nx.draw_networkx_edges(self.b2, b4, b12 = b7, edge_color=b15)
        nx.draw_networkx_edges(self.b2, b4, b12 = max(b7), edgelist=b14, edge_color='red')
        nx.draw_networkx_labels(self.b2, b4, b13 = 5, font_color='black', labels=b8)
        return b4