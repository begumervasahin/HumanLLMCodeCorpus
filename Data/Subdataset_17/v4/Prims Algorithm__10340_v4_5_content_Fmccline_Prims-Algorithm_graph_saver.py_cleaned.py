import networkx as nx
import matplotlib.pyplot as plt
import imageio
class GraphSaver:
    counter = 0
    def __init__(self, output_file, highlight_color='b', regular_color='r', node_color='r'):
        self.output_file = output_file
        self.highlight_color = highlight_color
        self.regular_color = regular_color
        self.node_color = node_color
    def save_highlighted_tree(self, graph, pos, tree_edges):
        new_graph = self._make_new_graph(graph, tree_edges)
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
    def _make_new_graph(self, graph, tree):
        new_graph = nx.Graph()
        edges_in_tree = {(from_node, to_node): True for from_node, to_node, weight in tree}
        edges_in_tree.update({(to_node, from_node): True for from_node, to_node, weight in tree})
        for from_node, to_node, weight in tree:
            new_graph.add_edge(from_node, to_node, weight=weight, color=self.highlight_color, width=8)
        for from_node, to_node, weight in graph.edges(data="weight"):
            if (from_node, to_node) not in edges_in_tree and (to_node, from_node) not in edges_in_tree:
                new_graph.add_edge(from_node, to_node, weight=weight, color=self.regular_color, width=2)
        return new_graph
    def save_gif(self, file_names):
        images = [imageio.imread(file_name) for file_name in file_names]
        output_file = f"{self.output_file}-gif.gif"
        imageio.mimsave(output_file, images, format="GIF", duration=2)