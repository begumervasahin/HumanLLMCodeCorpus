import networkx as nx
import matplotlib.pyplot as plt
def draw_graph_with_path(edges, path):
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    value_map = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    values = [value_map.get(node, 0.25) for node in G.nodes()]
    edge_labels = dict(((u, v), d['weight']) for u, v, d in G.edges(data=True))
    red_edges = path
    edge_colors = ['red' if edge in red_edges else 'black' for edge in G.edges()]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=values, node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=[e for e in G.edges() if e not in red_edges], arrows=False)
    plt.show()
if __name__ == "__main__":
    edges = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)]
    path = [(1, 2), (2, 3)]
    draw_graph_with_path(edges, path)