
import matplotlib.pyplot as plt
import networkx as nx
from prim import prim
def main():
    graph = nx.Graph()
    edges_with_weights = [
        ('A', 'B', 3), ('A', 'D', 5), ('A', 'E', 9),
        ('B', 'C', 5), ('B', 'D', 4), ('B', 'E', 8),
        ('C', 'D', 7), ('C', 'G', 3), ('D', 'F', 8),
        ('D', 'G', 5), ('D', 'H', 6), ('E', 'F', 2),
        ('F', 'H', 10), ('G', 'I', 1), ('H', 'I', 3)
    ]
    for edge in edges_with_weights:
        graph.add_edge(edge[0], edge[1], weight=edge[2])
    minimal_spanning_tree = prim(graph, 'A')
    other_edges = [edge for edge in graph.edges() if edge not in minimal_spanning_tree]
    print("Minimal Spanning Tree:", minimal_spanning_tree)
    node_positions = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, node_positions, node_size=500)
    nx.draw_networkx_edges(graph, node_positions, edgelist=minimal_spanning_tree, width=6)
    nx.draw_networkx_edges(graph, node_positions, edgelist=other_edges, width=6, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(graph, node_positions, font_size=20, font_family='sans-serif')
    plt.axis('off')
    plt.show()
if __name__ == "__main__":
    main()