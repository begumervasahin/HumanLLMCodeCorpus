import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b10, b11):
    b1 = nx.DiGraph()
    b1.add_weighted_edges_from(b10)
    b2 = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    b3 = [b2.get(node, 0.25) for node in b1.nodes()]
    b4 = {(u, v): data['weight'] for u, v, data in b1.b10(data=True)}
    b5 = ['red' if edge in b11 else 'black' for edge in b1.b10()]
    b6 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b6, b7 = b3, node_size=500, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(b1, b6, b8 = b11, edge_color='red', arrows=True)
    nx.draw_networkx_edges(b1, b6, b8 = [e for e in b1.b10() if e not in b11], edge_color='black', arrows=False)
    nx.draw_networkx_labels(b1, b6)
    nx.draw_networkx_edge_labels(b1, b6, b4 = b4)
    plt.show()
if b9 = = "__main__":
    b10 = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)]
    b11 = [(1, 2), (2, 3)]
    fonk1(b10, b11)