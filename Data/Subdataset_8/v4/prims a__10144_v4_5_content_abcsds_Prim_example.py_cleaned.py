
try:
    import matplotlib.pyplot as plt
    import networkx as nx
except ImportError as e:
    print("Error importing required libraries:", e)
    raise
from prim import prim
G = nx.Graph()
edges = [('A', 'B', 3), ('A', 'D', 5), ('A', 'E', 9), ('B', 'C', 5), ('B', 'D', 4), ('B', 'E', 8),
         ('C', 'D', 7), ('C', 'G', 3), ('D', 'F', 8), ('D', 'G', 5), ('D', 'H', 6), ('E', 'F', 2),
         ('F', 'H', 10), ('G', 'I', 1), ('H', 'I', 3)]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])
mst = prim(G, 'A')
other_edges = [n for n in G.edges() if n not in mst]
print("Minimal Spanning Tree:", mst)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=mst, width=6)
nx.draw_networkx_edges(G, pos, edgelist=other_edges, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()