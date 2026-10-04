
import matplotlib.pyplot as plt
import networkx as nx
def visualize_graph(edges, node_labels=None, title="Graph Visualization"):
    """
    Visualizes a graph using NetworkX and Matplotlib.
    Parameters:
    - edges (list of tuples): List of edges in the graph. Each edge is represented as a tuple (node1, node2).
    - node_labels (dict, optional): Dictionary of node labels, where keys are nodes and values are labels.
    - title (str, optional): Title for the graph visualization. Defaults to "Graph Visualization".
    """
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    if node_labels:
        nx.draw(G, pos, with_labels=True, labels=node_labels, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold')
    else:
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos)
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    node_labels = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    visualize_graph(edges, node_labels, title="Sample Graph Visualization")