import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b11, b12):
    b1 = nx.DiGraph()
    b1.add_weighted_edges_from(b11)
    b2 = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    b3 = [b2.get(node, 0.25) for node in b1.nodes()]
    b4 = dict(((u, v), d['weight']) for u, v, d in b1.b11(data=True))
    b5 = b12
    b6 = ['red' if edge in b5 else 'black' for edge in b1.b11()]
    b7 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b7, b8 = plt.get_cmap('jet'), node_color=b3, node_size=500)
    nx.draw_networkx_edge_labels(b1, b7, b4 = b4)
    nx.draw_networkx_labels(b1, b7)
    nx.draw_networkx_edges(b1, b7, b9 = b5, edge_color='r', arrows=True)
    nx.draw_networkx_edges(b1, b7, b9 = [e for e in b1.b11() if e not in b5], arrows=False)
    plt.show()
if b10 = = "__main__":
    b11 = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)]
    b12 = [(1, 2), (2, 3)]
    fonk1(b11, b12)