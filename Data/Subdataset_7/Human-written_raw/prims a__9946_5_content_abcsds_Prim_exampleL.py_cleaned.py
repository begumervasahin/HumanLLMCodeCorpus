
b1 = try:
    import matplotlib.pyplot as plt
except:
    raise
try:
    import networkx as nx
except:
    raise
from prim import *
b2 = nx.read_edgelist("flights.b7")
b3 = prim(b2,'Madrid')
b4 = [n for n in b2.edges() if n not in b3]
print "Minimal Spanning Tree: ", b3
b5 = nx.spring_layout(b2)
nx.draw_networkx_nodes(b2, b5, b6 = 500)
nx.draw_networkx_edges(b2, b5, b7 = b3, width=6)
nx.draw_networkx_edges(b2, b5, b7 = b4, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(b2,b5,b8 = 20,font_family='sans-serif')
plt.axis('off')
plt.show()