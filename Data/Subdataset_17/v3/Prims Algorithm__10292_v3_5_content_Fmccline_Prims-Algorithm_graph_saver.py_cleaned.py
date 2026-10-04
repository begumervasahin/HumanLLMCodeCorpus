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
        highlighted_graph = self._create_highlighted_graph(graph, tree_edges)
        file_name = f"{self.output_file}-{GraphSaver.counter}.png"
        self._draw_and_save_graph(highlighted_graph, pos, file_name)
        GraphSaver.counter += 1
        return file_name
    def _create_highlighted_graph(self, graph, tree_edges):
        new_graph = nx.Graph()
        tree_edge_set = set((u, v) for u, v, _ in tree_edges)
        for from_node, to_node, weight in tree_edges:
            new_graph.add_edge(from_node, to_node, weight=weight, color=self.highlight_color, width=8)
        for from_node, to_node, weight in graph.edges(data="weight"):
            if (from_node, to_node) not in tree_edge_set and (to_node, from_node) not in tree_edge_set:
                new_graph.add_edge(from_node, to_node, weight=weight, color=self.regular_color, width=2)
        return new_graph
    def _draw_and_save_graph(self, graph, pos, file_name):
        edges = graph.edges()
        edge_colors = [graph[u][v]['color'] for u, v in edges]
        edge_widths = [graph[u][v]['width'] for u, v in edges]
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        plt.figure()
        nx.draw(graph, pos, edges=edges, edge_color=edge_colors, width=edge_widths)
        nx.draw_networkx_nodes(graph, pos, node_color=self.node_color)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        plt.savefig(file_name, format="png")
        plt.close()
    def save_gif(self, file_names):
        images = [imageio.imread(file_name) for file_name in file_names]
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