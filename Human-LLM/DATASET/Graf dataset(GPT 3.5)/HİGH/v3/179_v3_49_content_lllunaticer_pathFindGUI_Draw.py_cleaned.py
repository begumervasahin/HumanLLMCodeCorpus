import networkx as nx
import matplotlib.pyplot as plt
def fonk1(edges, path):
    b1 = nx.DiGraph()
    for edge in edges:
        source, target, b2 = edge
        b1.add_edge(source, target, b2 = b2)
    b3 = {1: 1.0, 2: 0.5714285714285714, 3: 0.0}
    b4 = [b3.get(node, 0.25) for node in b1.nodes()]
    b5 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b5, b6 = plt.get_cmap('jet'), node_color=b4, node_size=500)
    b7 = {(u, v): d['b2'] for u, v, d in b1.edges(data=True)}
    nx.draw_networkx_edge_labels(b1, b5, b7 = b7)
    nx.draw_networkx_labels(b1, b5)
    b8 = path
    b9 = ['black' if edge not in b8 else 'red' for edge in b1.edges()]
    nx.draw_networkx_edges(b1, b5, b10 = b8, edge_color='r', arrows=True)
    nx.draw_networkx_edges(b1, b5, b10 = [edge for edge in b1.edges() if edge not in b8], edge_color=b9, arrows=False)
    plt.show()
