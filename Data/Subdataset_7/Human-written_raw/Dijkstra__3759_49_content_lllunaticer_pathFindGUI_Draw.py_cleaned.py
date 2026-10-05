import networkx as nx
import matplotlib.pyplot as plt
def fonk1(w,path):
    b1 = nx.DiGraph()
    for li in w:
        b1.add_weighted_edges_from([(li[0], li[1], li[2])])
    b2 = {1: 1.0,
               4: 0.5714285714285714,
               8: 0.0}
    b3 = [b2.get(node, 0.25) for node in b1.nodes()]
    b4 = dict([((u, v,), d['weight'])
                        for u, v, d in b1.edges(b5 = True)])
    b6 = path
    b7 = ['black' if not edge in b6 else 'red'
                    for edge in b1.edges()]
    b8 = [edge for edge in b1.edges() if edge not in b6]
    b9 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b9, b10 = plt.get_cmap('jet'),
                           b11 = b3, node_size=500)
    nx.draw_networkx_edge_labels(b1, b9, b4 = b4)
    nx.draw_networkx_labels(b1, b9)
    nx.draw_networkx_edges(b1, b9, b12 = b6, edge_color='r', arrows=True)
    nx.draw_networkx_edges(b1, b9, b12 = b8, arrows=False)
    plt.show()