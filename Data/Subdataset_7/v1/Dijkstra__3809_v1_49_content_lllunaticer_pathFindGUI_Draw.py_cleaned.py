import networkx as nx
import matplotlib.pyplot as plt
def fonk1(edges, path):
    b1 = nx.DiGraph()
    for edge in edges:
        b1.add_weighted_edges_from([edge])
    b2 = [1.0, 0.5714285714285714, 0.0]
    b3 = [b2.get(node, 0.25) for node in b1.nodes()]
    b4 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b4, b5 = plt.get_cmap('jet'), node_color=b3, node_size=500)
    b6 = {(u, v): d['weight'] for u, v, d in b1.edges(data=True)}
    nx.draw_networkx_edge_labels(b1, b4, b6 = b6)
    nx.draw_networkx_labels(b1, b4)
    b7 = path
    b8 = ['black' if edge not in b7 else 'red' for edge in b1.edges()]
    nx.draw_networkx_edges(b1, b4, b9 = b7, edge_color='r', arrows=True)
    nx.draw_networkx_edges(b1, b4, b9 = [edge for edge in b1.edges() if edge not in b7], edge_color=b8, arrows=False)
    plt.show()
