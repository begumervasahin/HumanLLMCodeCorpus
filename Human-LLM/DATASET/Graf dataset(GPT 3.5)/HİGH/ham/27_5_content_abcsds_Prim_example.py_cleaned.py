
b1 = try:
    import matplotlib.pyplot as plt
except:
    raise
try:
    import networkx as nx
except:
    raise
from prim import *
b2 = nx.Graph()
b2.add_edge('A','B',b3 = 3)
b2.add_edge('A','D',b3 = 5)
b2.add_edge('A','E',b3 = 9)
b2.add_edge('B','C',b3 = 5)
b2.add_edge('B','D',b3 = 4)
b2.add_edge('B','E',b3 = 8)
b2.add_edge('C','D',b3 = 7)
b2.add_edge('C','b2',b3 = 3)
b2.add_edge('D','F',b3 = 8)
b2.add_edge('D','b2',b3 = 5)
b2.add_edge('D','H',b3 = 6)
b2.add_edge('E','F',b3 = 2)
b2.add_edge('F','H',b3 = 10)
b2.add_edge('b2','I',b3 = 1)
b2.add_edge('H','I',b3 = 3)
b4 = prim(b2,'A')
b5 = [n for n in b2.edges() if n not in b4]
print "Minimal Spanning Tree: ", b4
b6 = nx.spring_layout(b2)
nx.draw_networkx_nodes(b2, b6, b7 = 500)
nx.draw_networkx_edges(b2, b6, b8 = b4, width=6)
nx.draw_networkx_edges(b2, b6, b8 = b5, width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(b2,b6,b9 = 20,font_family='sans-serif')
plt.axis('off')
plt.show()