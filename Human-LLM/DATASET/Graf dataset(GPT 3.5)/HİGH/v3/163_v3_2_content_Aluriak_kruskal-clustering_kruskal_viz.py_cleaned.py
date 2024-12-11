import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b2):
    nx.draw(b2, b1 = True, node_color='skyblue', node_size=1000, font_size=12)
    plt.title("Graph Visualization")
    plt.show()
def fonk2():
    b2 = nx.Graph()
    b2.add_nodes_from([1, 2, 3, 4, 5])
    b2.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
    return b2
if b3 = = "__main__":
    b2 = fonk2()
    fonk1(b2)