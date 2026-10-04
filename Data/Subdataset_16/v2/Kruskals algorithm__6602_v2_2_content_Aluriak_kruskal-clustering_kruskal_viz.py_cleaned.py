
import matplotlib.pyplot as plt
import networkx as nx
def fonk1(b8, b1 = None, b9="Graph Visualization"):
    """
    Visualizes a graph using NetworkX and Matplotlib.
    Parameters:
    - b8 (list of tuples): List of b8 in the graph. Each edge is represented as a tuple (node1, node2).
    - b1 (dict, optional): Dictionary of node labels, where keys are nodes and values are labels.
    - b9 (str, optional): Title for the graph visualization. Defaults to "Graph Visualization".
    """
    b2 = nx.Graph()
    b2.add_edges_from(b8)
    b3 = nx.spring_layout(b2)
    if b1:
        nx.draw(
            b2, b3, b4 = True, labels=b1,
            b5 = 'lightblue', node_size=3000,
            b6 = 12, font_weight='bold'
        )
    else:
        nx.draw(
            b2, b3, b4 = True,
            b5 = 'lightblue', node_size=3000,
            b6 = 12, font_weight='bold'
        )
    nx.draw_networkx_edges(b2, b3)
    plt.b9(b9)
    plt.show()
if b7 = = "__main__":
    b8 = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    b1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    fonk1(b8, b1, b9 = "Sample Graph Visualization")