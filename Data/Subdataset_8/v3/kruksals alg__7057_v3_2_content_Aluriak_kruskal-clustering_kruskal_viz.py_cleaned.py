import networkx as nx
import matplotlib.pyplot as plt
def visualize_graph(graph):
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
    plt.title("Graph Visualization")
    plt.show()
def create_sample_graph():
    graph = nx.Graph()
    graph.add_nodes_from([1, 2, 3, 4, 5])
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
    return graph
if __name__ == "__main__":
    graph = create_sample_graph()
    visualize_graph(graph)