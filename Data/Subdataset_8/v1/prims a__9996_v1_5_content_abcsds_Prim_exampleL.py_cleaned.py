try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib library is required. Install it using 'pip install matplotlib'")
try:
    import networkx as nx
except ImportError:
    raise ImportError("NetworkX library is required. Install it using 'pip install networkx'")
from prim import prim
G = nx.read_edgelist("flights.edgelist")
mst = prim(G, 'Madrid')
othr = [n for n in G.edges() if n not in mst]
print("Minimal Spanning Tree: ", mst)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=mst, width=6)
nx.draw_networkx_edges(G, pos, edgelist=othr, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()