import networkx as nx
import matplotlib.pyplot as plt
def draw_graph_with_path(edges, path):
    G = nx.DiGraph()
    for edge in edges:
        source, target, weight = edge
        G.add_weighted_edges_from([(source, target, weight)])
    node_values = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    node_colors = [node_values.get(node, 0.25) for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=node_colors, node_size=500)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos)
    red_edges = path
    edge_colors = ['black' if edge not in red_edges else 'red' for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=[edge for edge in G.edges() if edge not in red_edges], arrows=False)
    plt.show()
