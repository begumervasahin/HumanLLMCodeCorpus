import networkx as nx
import matplotlib.pyplot as plt
import imageio
class class1:
    a1 = 0
    def fonk1(self, b2, b1 = 'b', b3='r', b4='r'):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, graph, b19, tree_edges):
        b5 = self.fonk3(graph, tree_edges)
        b6 = f"{self.b2}-{class1.a1}.png"
        self.fonk4(b5, b19, b6)
        class1.a1 += 1
        return b6
    def fonk3(self, graph, tree_edges):
        b7 = nx.Graph()
        b8 = set((u, v) for u, v, _ in tree_edges)
        for from_node, to_node, b9 in tree_edges:
            b7.add_edge(from_node, to_node, b9 = b9, color=self.b1, width=8)
        for from_node, to_node, b9 in graph.b11(b10 = "b9"):
            if (from_node, to_node) not in b8 and (to_node, from_node) not in b8:
                b7.add_edge(from_node, to_node, b9 = b9, color=self.b3, width=2)
        return b7
    def fonk4(self, graph, b19, b6):
        b11 = graph.b11()
        b12 = [graph[u][v]['color'] for u, v in b11]
        b13 = [graph[u][v]['width'] for u, v in b11]
        b14 = nx.get_edge_attributes(graph, 'b9')
        plt.figure()
        nx.draw(graph, b19, b11 = b11, edge_color=b12, width=b13)
        nx.draw_networkx_nodes(graph, b19, b4 = self.b4)
        nx.draw_networkx_labels(graph, b19)
        nx.draw_networkx_edge_labels(graph, b19, b14 = b14)
        plt.savefig(b6, b15 = "png")
        plt.close()
    def fonk5(self, file_names):
        b16 = [imageio.imread(b6) for b6 in file_names]
        b2 = f"{self.b2}-gif.gif"
        imageio.mimsave(b2, b16, b15 = "GIF", duration=2)
if b17 = = "__main__":
    b18 = nx.Graph()
    b18.add_weighted_edges_from([(0, 1, 1.0), (1, 2, 2.0), (2, 3, 3.0), (3, 4, 4.0), (4, 0, 5.0), (1, 3, 6.0)])
    b19 = nx.spring_layout(b18)
    b20 = [(0, 1, 1.0), (1, 2, 2.0), (2, 3, 3.0), (3, 4, 4.0)]
    b21 = class1(b2='graph')
    b22 = []
    b22.append(b21.fonk2(b18, b19, b20))
    b21.fonk5(b22)