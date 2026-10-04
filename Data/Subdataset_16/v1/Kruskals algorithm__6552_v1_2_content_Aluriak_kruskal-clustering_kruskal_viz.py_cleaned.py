
import matplotlib.pyplot as plt
import networkx as nx
def fonk1(b6, b1 = None, b7="Graph Visualization"):
    """
    Visualizes a graph using NetworkX and Matplotlib.
    Parameters:
    - b6 (list of tuples): List of b6 in the graph. Each edge is represented as a tuple (node1, node2).
    - b1 (dict, optional): Dictionary of node labels, where keys are nodes and values are labels.
    - b7 (str, optional): Title for the graph visualization. Defaults to "Graph Visualization".
    """
    b2 = nx.Graph()
    b2.add_edges_from(b6)
    b3 = nx.spring_layout(b2)
    if b1:
        nx.draw(b2, b3, b4 = True, labels=b1, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold')
    else:
        nx.draw(b2, b3, b4 = True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(b2, b3)
    plt.b7(b7)
    plt.show()
if b5 = = "__main__":
    b6 = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    b1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    fonk1(b6, b1, b7 = "Sample Graph Visualization")