
import matplotlib.pyplot as plt
import networkx as nx
def fonk1(b2, b1 = None, b3="Graph Visualization"):
    """
    Visualizes a graph using NetworkX and Matplotlib.
    Parameters:
    - b2 (list of tuples): List of b2 in the graph. Each edge is represented as a tuple (node1, node2).
    - b1 (dict, optional): Dictionary of node labels, where keys are nodes and values are labels.
    - b3 (str, optional): Title for the graph visualization. Defaults to "Graph Visualization".
    Example usage of visualize_graph function.
    """
    b2 = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    b1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    fonk1(b2, b1, b3 = "Sample Graph Visualization")
if b4 = = "__main__":
    main()