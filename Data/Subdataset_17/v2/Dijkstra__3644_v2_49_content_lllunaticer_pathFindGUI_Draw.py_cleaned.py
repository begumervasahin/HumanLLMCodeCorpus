import networkx as nx
import matplotlib.pyplot as plt
def draw_graph_with_path(edges, path):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)
    value_map = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    node_colors = [value_map.get(node, 0.25) for node in graph.nodes()]
    edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    edge_colors = ['red' if edge in path else 'black' for edge in graph.edges()]
    positions = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, positions, node_color=node_colors, node_size=500, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(graph, positions, edgelist=path, edge_color='r', arrows=True)
    nx.draw_networkx_edges(graph, positions, edgelist=[e for e in graph.edges() if e not in path], edge_color='black', arrows=False)
    nx.draw_networkx_labels(graph, positions)
    nx.draw_networkx_edge_labels(graph, positions, edge_labels=edge_labels)
    plt.show()
if __name__ == "__main__":
    edges = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (3, 4, 5)]
    path = [(1, 2), (2, 3)]
    draw_graph_with_path(edges, path)