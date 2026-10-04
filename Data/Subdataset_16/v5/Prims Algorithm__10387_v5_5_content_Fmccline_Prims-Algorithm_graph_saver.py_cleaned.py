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
    def fonk2(self, graph, pos, tree_edges):
        b5 = self.fonk3(graph, tree_edges)
        self.fonk4(b5, pos)
        b6 = f"{self.b2}-{self.a1}.png"
        plt.savefig(b6, b7 = "png")
        plt.close()
        self.a1 += 1
        return b6
    def fonk3(self, graph, tree_edges):
        b8 = nx.Graph()
        b9 = {(from_node, to_node) for from_node, to_node, b10 in tree_edges}
        b9.update({(to_node, from_node) for from_node, to_node, b10 in tree_edges})
        for from_node, to_node, b10 in tree_edges:
            b8.add_edge(from_node, to_node, b10 = b10, color=self.b1, width=8)
        for from_node, to_node, b10 in graph.b12(b11 = "b10"):
            if (from_node, to_node) not in b9 and (to_node, from_node) not in b9:
                b8.add_edge(from_node, to_node, b10 = b10, color=self.b3, width=2)
        return b8
    def fonk4(self, graph, pos):
        b12 = graph.b12()
        b13 = [graph[u][v]['color'] for u, v in b12]
        b14 = [graph[u][v]['width'] for u, v in b12]
        b15 = nx.get_edge_attributes(graph, 'b10')
        plt.figure()
        nx.draw(graph, pos, b12 = b12, edge_color=b13, width=b14)
        nx.draw_networkx_nodes(graph, pos, b4 = self.b4)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, b16 = b15)
    def fonk5(self, file_names):
        b17 = [imageio.imread(b6) for b6 in file_names]
        b2 = f"{self.b2}-gif.gif"
        imageio.mimsave(b2, b17, b7 = "GIF", duration=2)