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
        b6 = b5.b6()
        b7 = [b5[u][v]['color'] for u, v in b6]
        b8 = [b5[u][v]['width'] for u, v in b6]
        b9 = nx.get_edge_attributes(b5, 'b14')
        plt.figure()
        nx.draw(b5, pos, b6 = b6, edge_color=b7, width=b8)
        nx.draw_networkx_nodes(b5, pos, b4 = self.b4)
        nx.draw_networkx_labels(b5, pos)
        nx.draw_networkx_edge_labels(b5, pos, b10 = b9)
        b11 = f"{self.b2}-{self.a1}.png"
        plt.savefig(b11, b12 = "png")
        plt.close()
        self.a1 += 1
        return b11
    def fonk3(self, graph, tree):
        b5 = nx.Graph()
        b13 = {(from_node, to_node): True for from_node, to_node, b14 in tree}
        b13.update({(to_node, from_node): True for from_node, to_node, b14 in tree})
        for from_node, to_node, b14 in tree:
            b5.add_edge(from_node, to_node, b14 = b14, color=self.b1, width=8)
        for from_node, to_node, b14 in graph.b6(b15 = "b14"):
            if (from_node, to_node) not in b13 and (to_node, from_node) not in b13:
                b5.add_edge(from_node, to_node, b14 = b14, color=self.b3, width=2)
        return b5
    def fonk4(self, file_names):
        b16 = [imageio.imread(b11) for b11 in file_names]
        b2 = f"{self.b2}-gif.gif"
        imageio.mimsave(b2, b16, b12 = "GIF", duration=2)