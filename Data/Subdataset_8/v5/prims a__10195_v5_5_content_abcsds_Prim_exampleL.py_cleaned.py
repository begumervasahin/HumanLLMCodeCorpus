import matplotlib.pyplot as plt
import networkx as nx
from prim import prim
try:
    import matplotlib.pyplot as plt
    import networkx as nx
except ImportError as e:
    raise ImportError("Required libraries not found:", e)
try:
    G = nx.read_edgelist("flights.edgelist")
except FileNotFoundError:
    raise FileNotFoundError("Edgelist file not found")
minimal_spanning_tree = prim(G, 'Madrid')
other_edges = [edge for edge in G.edges() if edge not in minimal_spanning_tree]
print("Minimal Spanning Tree:", minimal_spanning_tree)
layout = nx.spring_layout(G)
nx.draw_networkx_nodes(G, layout, node_size=500)
nx.draw_networkx_edges(G, layout, edgelist=minimal_spanning_tree, width=6)
nx.draw_networkx_edges(G, layout, edgelist=other_edges, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(G, layout, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()