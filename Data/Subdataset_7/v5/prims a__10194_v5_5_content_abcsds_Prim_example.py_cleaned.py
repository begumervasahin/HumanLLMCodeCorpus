
import matplotlib.pyplot as plt
import networkx as nx
from prim import prim
def fonk1():
    b1 = nx.Graph()
    b2 = [
        ('A', 'B', 3), ('A', 'D', 5), ('A', 'E', 9),
        ('B', 'C', 5), ('B', 'D', 4), ('B', 'E', 8),
        ('C', 'D', 7), ('C', 'G', 3), ('D', 'F', 8),
        ('D', 'G', 5), ('D', 'H', 6), ('E', 'F', 2),
        ('F', 'H', 10), ('G', 'I', 1), ('H', 'I', 3)
    ]
    for edge in b2:
        b1.add_edge(edge[0], edge[1], b3 = edge[2])
    b4 = prim(b1, 'A')
    b5 = [edge for edge in b1.edges() if edge not in b4]
    print("Minimal Spanning Tree:", b4)
    b6 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b6, b7 = 500)
    nx.draw_networkx_edges(b1, b6, b8 = b4, width=6)
    nx.draw_networkx_edges(b1, b6, b8 = b5, width=6, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(b1, b6, b9 = 20, font_family='sans-serif')
    plt.axis('off')
    plt.show()
if b10 = = "__main__":
    fonk1()