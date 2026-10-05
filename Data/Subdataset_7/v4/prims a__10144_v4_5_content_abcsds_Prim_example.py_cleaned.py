
try:
    import matplotlib.pyplot as plt
    import networkx as nx
except ImportError as e:
    print("Error importing required libraries:", e)
    raise
from prim import prim
b1 = nx.Graph()
b2 = [('A', 'B', 3), ('A', 'D', 5), ('A', 'E', 9), ('B', 'C', 5), ('B', 'D', 4), ('B', 'E', 8),
         ('C', 'D', 7), ('C', 'b1', 3), ('D', 'F', 8), ('D', 'b1', 5), ('D', 'H', 6), ('E', 'F', 2),
         ('F', 'H', 10), ('b1', 'I', 1), ('H', 'I', 3)]
for edge in b2:
    b1.add_edge(edge[0], edge[1], b3 = edge[2])
b4 = prim(b1, 'A')
b5 = [n for n in b1.b2() if n not in b4]
print("Minimal Spanning Tree:", b4)
b6 = nx.spring_layout(b1)
nx.draw_networkx_nodes(b1, b6, b7 = 500)
nx.draw_networkx_edges(b1, b6, b8 = b4, width=6)
nx.draw_networkx_edges(b1, b6, b8 = b5, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(b1, b6, b9 = 20, font_family='sans-serif')
plt.axis('off')
plt.show()