import networkx as nx
import matplotlib.pyplot as plt
def draw_graph_with_path(weighted_edges, highlighted_path):
    graph = nx.DiGraph()
    for edge in weighted_edges:
        source, target, weight = edge
        graph.add_weighted_edges_from([(source, target, weight)])
    node_values = {1: 1.0, 4: 0.5714285714285714, 8: 0.0}
    node_colors = [node_values.get(node, 0.25) for node in graph.nodes()]
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_color=node_colors, node_size=500)
    edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(graph, pos)
    red_edges = highlighted_path
    edge_colors = ['black' if edge not in red_edges else 'red' for edge in graph.edges()]
    nx.draw_networkx_edges(graph, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(graph, pos, edgelist=[edge for edge in graph.edges() if edge not in red_edges], arrows=False)
    plt.show()
