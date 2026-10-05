import networkx as nx
import matplotlib.pyplot as plt
def visualize_graph(graph):
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
    plt.title("Graph Visualization")
    plt.show()
if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_nodes_from([1, 2, 3, 4, 5])
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
    visualize_graph(graph)