import networkx as nx
import matplotlib.pyplot as plt
import imageio
class GraphSaver():
    counter = 0
    def __init__(self, output_file, highlight_color='b', regular_color='r', node_color='r'):
        self.output_file = output_file
        self.highlight_color = highlight_color
        self.regular_color = regular_color
        self.node_color = node_color
    def save_highlighted_tree(self, graph, pos, tree_edges):
        new_graph = self.__make_new_graph(graph, tree_edges)
        edges = new_graph.edges()
        colors = [new_graph[u][v]['color'] for u, v in edges]
        widths = [new_graph[u][v]['width'] for u, v in edges]
        labels = nx.get_edge_attributes(new_graph, 'weight')
        plt.figure()
        nx.draw(new_graph, pos, edges=edges, edge_color=colors, width=widths)
        nx.draw_networkx_nodes(new_graph, pos, node_color=self.node_color)
        nx.draw_networkx_labels(new_graph, pos)
        nx.draw_networkx_edge_labels(new_graph, pos, edge_labels=labels)
        file_name = f"{self.output_file}-{self.counter}.png"
        plt.savefig(file_name, format="png")
        plt.close()
        self.counter += 1
        return file_name
    def __make_new_graph(self, graph, tree):
        new_graph = nx.Graph()
        edges_in_tree = {}
        for from_node, to_node, weight in tree:
            new_graph.add_edge(from_node, to_node, weight=weight, color=self.highlight_color, width=8)
            edges_in_tree[(from_node, to_node)] = True
            edges_in_tree[(to_node, from_node)] = True
        for from_node, to_node, weight in graph.edges(data="weight"):
            if (from_node, to_node) in edges_in_tree or (to_node, from_node) in edges_in_tree:
                continue
            else:
                new_graph.add_edge(from_node, to_node, weight=weight, color=self.regular_color, width=2)
        return new_graph
    def save_gif(self, file_names):
        images = []
        for file_name in file_names:
            image = imageio.imread(file_name)
            images.append(image)
        output_file = f"{self.output_file}-gif.gif"
        imageio.mimsave(output_file, images, format="GIF", duration=2)
if __name__ == "__main__":
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 1.0), (1, 2, 2.0), (2, 3, 3.0), (3, 4, 4.0), (4, 0, 5.0), (1, 3, 6.0)])
    pos = nx.spring_layout(G)
    mst_edges = [(0, 1, 1.0), (1, 2, 2.0), (2, 3, 3.0), (3, 4, 4.0)]
    graph_saver = GraphSaver(output_file='graph')
    png_files = []
    png_files.append(graph_saver.save_highlighted_tree(G, pos, mst_edges))
    graph_saver.save_gif(png_files)