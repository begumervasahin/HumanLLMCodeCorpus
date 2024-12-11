import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b3):
    nx.draw(b3, b1 = True, node_color='skyblue', node_size=1000, font_size=12)
    plt.title("Graph Visualization")
    plt.show()
if b2 = = "__main__":
    b3 = nx.Graph()
    b3.add_nodes_from([1, 2, 3, 4, 5])
    b3.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
    fonk1(b3)